#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

This looks like a runtime complexity of O(n). The loop has to run n number of times , but that's it. the a variable is incremented using whatever n is used in the loop.
b)

Looks like a runtime complexity starts out as O(n) in the outer loop. However, the runtime complexity of the inner `while` loop is hard. The outer loop is liner with O(n), but the inner loop is incremental. The increments aren't additions though, they are multiplications. So that would mean that it could technically grow twice as fast. This would halve the runtime if n=10, because jwould hit 10 after only going through four loops. I think that makes that runtime log(n). Combining these two runtimes would be O(n*log(n))

c) This is recursive. It also looks like for every n, the recursion will do n-1 for every time that the function is called, meaning that the runtime for this is O(n).

## Exercise II

This looks like a prime candidate for some binary searching. Halving the number of viable floors by starting at the absoulte middle floor will help us to save more eggs and quickly arrive at the maximum safe height.

f is going to be n//2. That's the first and biggest 'halving' that we'll do. Drop the egg. If it breaks, you need to go halfway DOWN the building and try the next floor (n//2)

if it doesn't break, you need to turn around and go half the distance UP the remaining floors until you reach the middle of those, where you'll drop another egg.

You will repeat either of the both above steps until you reach the maximum safe height for the egg. That floor is safe, and the next floor above (+1) is where it would break.

This is recursion, and the runtime would be O(n)
