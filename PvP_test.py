from PvP import PvP


def test_pvp_valid_input():
    # Arrange
    pvp = PvP()
    # Act & Assert
    assert pvp.valid_input(1, 4)
    assert pvp.valid_input(2, 4)
    assert pvp.valid_input(3, 4)
    assert not pvp.valid_input(4, 4)
    assert not pvp.valid_input(0, 1)


def test_win():
    pvp = PvP()
    assert pvp.win('foo', 1)
    assert not pvp.win('foo', 2)


def test_switch_player():
    pvp = PvP()
    pvp.switch_player()
    assert pvp.player == 2


def test_valid_num_of_sticks():
    pvp = PvP()
    assert pvp.valid_num_of_sticks(20)
    assert pvp.valid_num_of_sticks(30)
    assert pvp.valid_num_of_sticks(50)
    assert pvp.valid_num_of_sticks(70)
    assert not pvp.valid_num_of_sticks(110)
