import copy
from enum import Enum


sample_data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


CARD_RANKINGS = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}
HAND_RANKINGS = {
    "five of a kind": 7,
    "four of a kind": 6,
    "full house": 5,
    "three of a kind": 4,
    "two pair": 3,
    "one pair": 2,
    "high card": 1,
}


class HandTypes(Enum):
    five_of_a_kind = "five of a kind"
    four_of_a_kind = "four of a kind"
    full_house = "full house"
    three_of_a_kind = "three of a kind"
    two_pair = "two pair"
    one_pair = "one pair"
    high_card = "high card"


class Hand(object):
    def __init__(self, cards: str, bid: int) -> None:
        self.cards = cards
        self.bid = bid

    @property
    def type(self) -> str:
        type = ""

        working_hand = copy.copy(self._joker_transform(self.cards))

        unique_cards = set(working_hand)

        match len(unique_cards):
            case 1:
                # Can only be five of a kind.
                type = HandTypes.five_of_a_kind.value
            case 2:
                # Can be either four of a kind or full house.
                if (
                    working_hand.count(sorted(list(unique_cards))[0]) == 4
                    or working_hand.count(sorted(list(unique_cards))[0]) == 1
                ):
                    type = HandTypes.four_of_a_kind.value
                else:
                    type = HandTypes.full_house.value
            case 3:
                # Can be either three of a kind or two pair.
                counts = [
                    working_hand.count(x)
                    for x in unique_cards
                    if len(unique_cards) == 3
                ]
                if 3 in counts:
                    type = HandTypes.three_of_a_kind.value
                else:
                    type = HandTypes.two_pair.value
            case 4:
                # Can only be one pair.
                type = HandTypes.one_pair.value
            case 5:
                # Can only be high card.
                type = HandTypes.high_card.value

        if self.cards != working_hand:
            print(self.cards, " ---> ", working_hand, type)

        return type

    def _joker_transform(self, cards: str) -> str:
        transform = cards
        if "J" in cards and cards.count("J") < 5:
            # print(cards)
            counts = {c: [] for c in range(1, len(cards) + 1)}
            for card in cards:
                if card not in counts[cards.count(card)] and card != "J":
                    counts[cards.count(card)].append(card)
            highest_value = max([x for x in counts.keys() if counts[x] != []])
            transform = cards.replace("J", counts[highest_value][0])

        return transform


def go(data):
    # data = sample_data
    hands = [Hand(cards=x.split()[0], bid=int(x.split()[1])) for x in data.splitlines()]
    hands.sort(key=lambda y: HAND_RANKINGS[y.type])

    sorted = []

    for _, t in enumerate(HandTypes):
        hands_of_type = list(filter(lambda z: z.type == t.value, hands))
        hands_of_type.sort(
            reverse=True,
            key=lambda h: (
                CARD_RANKINGS[h.cards[0]],
                CARD_RANKINGS[h.cards[1]],
                CARD_RANKINGS[h.cards[2]],
                CARD_RANKINGS[h.cards[3]],
                CARD_RANKINGS[h.cards[4]],
            ),
        )

        sorted.extend(hands_of_type)

    answer = 0

    for j, h in enumerate(sorted):
        answer += (len(sorted) - j) * h.bid
        # print(h.type, h.cards)

    if answer >= 253104988:
        print("Too high")

    print("Answer:", answer)

    return answer
