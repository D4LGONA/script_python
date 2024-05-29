import itertools
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.N = 0

    def inHand(self):
        return self.N

    def addCard(self, c):
        self.cards.append(c)
        self.N += 1

    def reset(self):
        self.N = 0
        self.cards.clear()

    def card_value(self, card):
        return 14 if card.value == 1 else card.value

    def is_straight(self, cards):
        values = sorted(set(self.card_value(card) for card in cards))
        if len(values) < 5:
            return False
        if values[-5:] == [10, 11, 12, 13, 14]:
            return True
        for i in range(len(values) - 4):
            if values[i:i + 5] == list(range(values[i], values[i] + 5)):
                return True
        return False

    def is_flush(self, cards):
        suits = [card.getsuit() for card in cards]
        for suit in ["Clubs", "Spades", "Hearts", "Diamonds"]:
            if suits.count(suit) >= 5:
                return True
        return False

    def is_straight_flush(self, cards):
        for suit in ["Clubs", "Spades", "Hearts", "Diamonds"]:
            suited_cards = [card for card in cards if card.getsuit() == suit]
            if len(suited_cards) >= 5 and self.is_straight(suited_cards):
                return True
        return False

    def kind_count(self, cards, n):
        values = [card.value for card in cards]
        return any(values.count(value) == n for value in range(1, 15))

    def is_four_of_a_kind(self, cards):
        return self.kind_count(cards, 4)

    def is_full_house(self, cards):
        values = [card.value for card in cards]
        three_kind = [value for value in range(1, 15) if values.count(value) == 3]
        pairs = [value for value in range(1, 15) if values.count(value) == 2]
        return len(three_kind) > 0 and len(pairs) > 0

    def is_three_of_a_kind(self, cards):
        return self.kind_count(cards, 3)

    def is_two_pair(self, cards):
        values = [card.value for card in cards]
        pairs = [value for value in range(1, 15) if values.count(value) == 2]
        return len(pairs) >= 2

    def is_one_pair(self, cards):
        return self.kind_count(cards, 2)

    def hand_rank(self, cards):
        if self.is_straight_flush(cards):
            straight_flush_cards = sorted(cards, key=lambda card: self.card_value(card), reverse=True)[:5]
            return (8, "Straight Flush", straight_flush_cards)
        if self.is_four_of_a_kind(cards):
            values = [self.card_value(card) for card in cards]
            four_kind_value = max(values, key=values.count)
            four_kind_cards = [card for card in cards if self.card_value(card) == four_kind_value]
            return (7, "Four of a Kind", four_kind_cards)
        if self.is_full_house(cards):
            values = [self.card_value(card) for card in cards]
            three_kind_value = max(values, key=values.count)
            pair_value = max(v for v in values if v != three_kind_value)
            full_house_cards = [card for card in cards if
                                self.card_value(card) == three_kind_value or self.card_value(card) == pair_value]
            three_kind_cards = [card for card in full_house_cards if self.card_value(card) == three_kind_value]
            pair_cards = [card for card in full_house_cards if self.card_value(card) == pair_value]
            return (6, "Full House", three_kind_cards + pair_cards)
        if self.is_flush(cards):
            suits = [card.getsuit() for card in cards]
            flush_suit = max(set(suits), key=suits.count)
            flush_cards = sorted([card for card in cards if card.getsuit() == flush_suit],
                                 key=lambda card: self.card_value(card), reverse=True)[:5]
            return (5, "Flush", flush_cards)
        if self.is_straight(cards):
            values = sorted(set(self.card_value(card) for card in cards))
            if values[-5:] == [10, 11, 12, 13, 14]:  # Handling the special case for Ace-high straight
                straight_cards = [card for card in cards if self.card_value(card) in [10, 11, 12, 13, 14]]
            else:
                for i in range(len(values) - 4):
                    if values[i:i + 5] == list(range(values[i], values[i] + 5)):
                        straight_values = values[i:i + 5]
                        break
                straight_cards = [card for card in cards if self.card_value(card) in straight_values]
            return (4, "Straight", sorted(straight_cards, key=lambda card: self.card_value(card), reverse=True)[:5])
        if self.is_three_of_a_kind(cards):
            values = [self.card_value(card) for card in cards]
            three_kind_value = max(values, key=values.count)
            three_kind_cards = [card for card in cards if self.card_value(card) == three_kind_value]
            return (3, "Three of a Kind", three_kind_cards)
        if self.is_two_pair(cards):
            values = [self.card_value(card) for card in cards]
            pairs = sorted([v for v in set(values) if values.count(v) == 2], reverse=True)[:2]
            pair_cards = [card for card in cards if self.card_value(card) in pairs]
            return (2, "Two Pair", pair_cards)
        if self.is_one_pair(cards):
            values = [self.card_value(card) for card in cards]
            pair_value = max(v for v in set(values) if values.count(v) == 2)
            pair_cards = [card for card in cards if self.card_value(card) == pair_value]
            return (1, "One Pair", pair_cards)
        high_cards = sorted(cards, key=lambda card: self.card_value(card), reverse=True)[:5]
        return (0, "High Card", high_cards)

    def best_hand(self):
        best = None
        best_rank = (-1, )
        for combo in itertools.combinations(self.cards, 5):
            rank = self.hand_rank(combo)
            if rank[0] > best_rank[0]:
                best = combo
                best_rank = rank
        return best

    def checking(self):
        if len(self.cards) < 7:
            return None, None, []  # 플레이어에게 카드가 충분하지 않은 경우
        best = self.best_hand()
        rank, hand_type, hand_values = self.hand_rank(best)
        return rank, hand_type, hand_values