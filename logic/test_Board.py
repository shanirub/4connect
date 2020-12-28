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


def test__check_horizontal():
    b = Board()
    player = 1
    assert b._check_horizontal(player, 3, 5) is False
    assert b.add_disc(player, 0)
    assert b.add_disc(player, 1)
    assert b._check_horizontal(player, 1, 5) is False
    assert b.add_disc(player, 2)
    assert b.add_disc(player, 3)
    assert b._check_horizontal(player, 3, 5)
    player = 2
    assert b.add_disc(player, 0)
    assert b.add_disc(player, 1)
    assert b._check_horizontal(player, 1, 4) is False
    assert b.add_disc(player, 2)
    assert b.add_disc(player, 3)
    assert b._check_horizontal(player, 3, 4)
    b1 = Board()
    assert b1._check_horizontal(player, 3, 5) is False
    assert b1.add_disc(player, 6)
    assert b1.add_disc(player, 5)
    assert b1.add_disc(player, 4)
    assert b1.add_disc(player, 3)
    assert b1._check_horizontal(player, 3, 5)


def test__check_diagonal_right():
    assert False
