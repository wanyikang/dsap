from doubly_linked_list import DoublyLinkedList

class PositionalList(DoublyLinkedList):
    """A sequential container of elements allowing positional access."""

    # nested Position class
    class Position:
        """An abstraction representing the location of a single element.

        Note that two position instaces may represent the same inherent
        location in the list.  Therefore, users should always rely on
        syntax 'p == q' rather than 'p is q' when testing equivalence of
        positions.
        """

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)               # opposite of __eq__

    # utility methods
    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:                  # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None                              # boundary violation
        else:
            return self.Position(self, node)         # legitimate position

    # accessors
    def first(self):
        """Return the first Position in the list (or None if list is empty)."""
        return self._make_position(self._header._next)

    def last(self):
        """Return the last Position in the list (or None if list is empty)."""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Return the Position just before Position p (or None if p is first)."""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Return the Position just after Position p (or None if p is last)."""
        node = self._validate(p)
        return self._make_position(node._next)

    def __len__(self):
        return super(PositionalList, self).__len__()

    def is_empty(self):
        return super(PositionalList, self).is_empty()

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def __reversed__(self):
        """Generate a backward iteration of the elements of the list."""
        cursor = self.last()
        while cursor is not None:
            yield cursor.element()
            cursor = self.before(cursor)

    # mutators
    # override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position."""
        node = super(PositionalList, self)._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return new Position."""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element e into list after Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self._validate(p)
        return self._delete_node(original)  # inherited method returns element

    def replace(self, p, e):
        """Replace the element at Position p with e.

        Return the element formerly at Position p.
        """
        original = self._validate(p)
        old_value = original._element  # temporarily store old element
        original._element = e  # replace with new element
        return old_value  # return the old element value

    def swap(self, pst_p, pst_q):
        """Swap element positions by p and q."""
        p = self._validate(pst_p)
        q = self._validate(pst_q)
        p_prev = p._prev
        p_next = p._next
        q_prev = q._prev
        q_next = q._next
        # modify q
        if q is not p_prev:
            p_prev._next = q
            q._prev = p_prev
        else:
            p_prev._next = p_next
            q._prev = p
        if q is not p_next:
            q._next = p_next
            p_next._prev = q
        else:
            q._next = p
            p_next._prev = p_prev
        # modify p
        if p is not q_prev:
            q_prev._next = p
            p._prev = q_prev
        else:
            q_prev._next = q_next
            p._prev = q
        if p is not q_next:
            q_next._prev = p
            p._next = q_next
        else:
            q_next._prev = q_prev
            p._next = q

if __name__ == '__main__':
    pl =  PositionalList()
    for i in range(10):
        pl.add_first(i)
    print(pl)

    for i in range(-1, -11, -1):
        pl.add_last(i)
    print(pl)

    pl.add_before(pl.first(), 10)
    print(pl)

    pl.add_after(pl.last(), -11)
    print(pl)

    pl.replace(pl.after(pl.after(pl.first())), 888)
    print(pl)

    p = pl.first()
    q = pl.after(p)
    pl.swap(p, q)
    print(pl)

    p = pl.first()
    q = pl.last()
    pl.swap(p, q)
    print(pl)

    print('len: ', len(pl))
    print('is_empty(): ', pl.is_empty())

