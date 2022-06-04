class Vector2D:
    def __init__(self, v: List[List[int]]):
        self.vector = v
        self.y = 0
        self.x = 0
    
    # If the current outer and inner point to an integer, this method does nothing.
    # Otherwise, inner and outer are advanced until they point to an integer.
    # If there are no more integers, then outer will be equal to vector.length
    # when this method terminates.
    def advance_to_next(self):
        # While outer is still within the vector, but inner is over the 
        # end of the inner list pointed to by outer, we want to move
        # forward to the start of the next inner vector.
        while self.x < len(self.vector) and self.y == len(self.vector[self.x]):
            self.x += 1
            self.y = 0
        
    def next(self) -> int:
        # Ensure the position pointers are moved such they point to an integer,
        # or put outer = vector.length.
        self.advance_to_next()
        # Return current element and move inner so that is after the current
        # element.
        result = self.vector[self.x][self.y]
        self.y += 1
        return result
        

    def hasNext(self) -> bool:
        # Ensure the position pointers are moved such they point to an integer,
        # or put outer = vector.length.
        self.advance_to_next()
        # If outer = vector.length then there are no integers left, otherwise
        # we've stopped at an integer and so there's an integer left.
        return self.x < len(self.vector)

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()


"""Java

public class Vector2D {

    private Iterator<List<Integer>> i;
    private Iterator<Integer> j;

    public Vector2D(List<List<Integer>> vec2d) {
        i = vec2d.iterator();
    }

    public int next() {
        hasNext();
        return j.next();
    }

    public boolean hasNext() {
        while ((j == null || !j.hasNext()) && i.hasNext())
            j = i.next().iterator();
        return j != null && j.hasNext();
    }
}
"""
