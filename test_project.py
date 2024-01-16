from project import initial_deal, generate_deck, reset
from classes.players import Human, Dealer


def test_generate_deck():
    assert "4♡" in generate_deck()
    assert "K♢" in generate_deck()
    assert "A♤" in generate_deck()
    assert "AA" not in generate_deck()
    assert "♢♤" not in generate_deck()

def test_initial_deal():
    deck = generate_deck()
    player = Human(wallet=100)
    dealer = Dealer()
    initial_deal(deck, player, dealer)
    assert len(deck) == 48
    assert len(deck) != 52
    assert len(player.hand) == 2
    assert len(player.hand) != 4

def test_reset():
    deck = generate_deck()
    player = Human(wallet=100)
    dealer = Dealer()
    initial_deal(deck, player, dealer)
    reset(player, dealer)
    assert len(player.hand) != 2
    assert len(player.hand) == 0
    assert len(dealer.hand) == 0