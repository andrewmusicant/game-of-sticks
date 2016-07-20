from PvC import PvC


def test_PvC_valid_input():
    # Arrange
    pvc = PvC()
    # Act & Assert
    assert pvc.valid_input(1, 4)
    assert pvc.valid_input(2, 4)
    assert pvc.valid_input(3, 4)
    assert not pvc.valid_input(4, 4)
    assert not pvc.valid_input(0, 1)


def test_win():
    pvc = PvC()
    assert pvc.win('foo', 1)
    assert not pvc.win('foo', 2)


def test_switch_player():
    pvc = PvC()
    pvc.switch_player()
    assert pvc.player == 'computer'


def test_valid_num_of_sticks():
    pvc = PvC()
    assert pvc.valid_num_of_sticks(20)
    assert pvc.valid_num_of_sticks(30)
    assert pvc.valid_num_of_sticks(50)
    assert pvc.valid_num_of_sticks(70)
    assert not pvc.valid_num_of_sticks(110)
