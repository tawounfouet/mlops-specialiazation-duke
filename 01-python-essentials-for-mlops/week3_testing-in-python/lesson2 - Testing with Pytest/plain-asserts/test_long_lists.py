

def test_long_lists():
  result = ['this', 'is', 'a', 'list', 'with', 'tons', 'of', 'items']
  expected = ['this', 'is', 'A', 'list', 'with', 'tons', 'of', 'items']
  assert result == expected