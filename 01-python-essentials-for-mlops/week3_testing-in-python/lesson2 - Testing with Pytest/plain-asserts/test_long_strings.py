
# pytest can be truly magical with its asserts, this is how it behaves with strings:

long_string = "This is A very long string that will need to be compared"

def test_long_string():
  expected = "This is a very long string that will need to be compared"
  assert long_string == expected