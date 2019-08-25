from services import shoplist

# OK -> None is Returned
def test_check_query01():
  result = shoplist.check_query("1-5")
  assert result is None

# OK -> Check Boundary Value
def test_check_query02():
  result = shoplist.check_query("0-1")
  assert result is None

# NG -> Check Boundary Value
def test_check_query03():
  result = shoplist.check_query("9-9")
  assert result == "E001"

# NG -> Check Boundary Value
def test_check_query04():
  result = shoplist.check_query("9-7")
  assert result == "E001"

# NG -> Query Not Range
def test_check_query05():
  result = shoplist.check_query("Hoge")
  assert result == "E002"
