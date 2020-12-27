from logic.Board import Board


def test_is_col_full():
    b = Board()
    assert b.is_col_full(0) is False


def test_has_won():
    assert False


def test_add_disc():
    b = Board()
    player = 1
    assert b.add_disc(player, 0)
    assert b.grid[5][0] == player
    assert b.add_disc(player, 0)
    assert b.grid[4][0] == player
    assert b.add_disc(player, 0)
    assert b.grid[3][0] == player


def test__check_vertical():
    assert True
