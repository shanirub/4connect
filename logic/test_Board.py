from logic.Board import Board


def test_is_col_full():
    b = Board()
    player = 1
    assert b.is_col_full(0) is False
    assert b.add_disc(player, 0)
    assert b.add_disc(player, 0)
    assert b.add_disc(player, 0)
    assert b.add_disc(player, 0)
    assert b.add_disc(player, 0)
    assert b.add_disc(player, 0)
    assert b.add_disc(player, 0) is False
    assert b.is_col_full(0) is True


def test_has_won():
    assert True


def test_add_disc():
    b = Board()
    player = 1
    assert b.add_disc(player, 0)
    assert b.grid[5][0] == player
    assert b.add_disc(player, 0)
    assert b.grid[4][0] == player
    assert b.add_disc(player, 0)
    assert b.grid[3][0] == player
    assert b.add_disc(player, 0)
    assert b.add_disc(player, 0)
    assert b.add_disc(player, 0)
    assert b.add_disc(player, 0) is False


def test__check_vertical():
    b = Board()
    player = 1
    assert b.add_disc(player, 0)
    assert b.add_disc(player, 0)
    assert b.add_disc(player, 0)
    assert b._check_vertical(1, 0, 3) is False
    assert b.add_disc(player, 0)
    assert b._check_vertical(1, 0, 2)
