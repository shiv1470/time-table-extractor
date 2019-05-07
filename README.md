# time-table-extractor
This would generate time table for asked faculty from a master time table

1. What does scratch1 do?

-> It takes Faculty code as input and prepare it's time-table from master time table which is much easier to read

2. What are algorithms used and how they decrease time complexity?

-> It uses Rabin Karp algorithm for string matching and reduces required time complexity to O(N+M) from O(N.M)

3. What are the modules it uses?

-> It uses XLRD module of python3 which enable users to read excel file in structured manner.

4. What does scratch2 do?

-> It takes input students and there registered subjects using file handling(Read mode) and make a graph where node denotes subject and an edge between subjects means both subjects cannot be scheduled on same day. It then generates a time table using minimum coloring.
