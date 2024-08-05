try:
    from task_2 import fn
except ImportError:
    fn = None
# Create a test to check if function exists
def test_fn_exists():
    assert hasattr(fn, '__call__'), 'Function not found'

def test_fn():
    assert fn(6) == 3.0, 'Wrong answer'