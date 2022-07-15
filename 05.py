'''
Author: Kavya Jain
Date: 14-06-2022
Day: Tuesday
Title: Patter Printing
'''

# -------------Square------------
# * * * *
# * * * *
# * * * *
# * * * *
# a = int(input("Enter the no. of rows: "))
# for i in range(0, a):
#     for j in range(0, a):
#         print("* ", end="")
#     print()


# -------------Rectangle----------------
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# a = int(input("Enter the no. of rows: ")) 
# b = int(input("Enter the no. of columns: ")) 
# for i in range(0, a):
#     for j in range(0, b):
#         print("* ", end="")
#     print()

# ----------Right-Angled Triangle / Half Pyramid------------
#    1 2 3 4           i    j               j <= i
#  1 *                 1    1               j <= 1
#  2 * *               2    1, 2            j <= 2
#  3 * * *             3    1, 2, 3         j <= 3
#  4 * * * *           4    1, 2, 3, 4      j <= 4
# n = int(input("Enter the no. of rows: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if j <= i:
#             print("* ", end="")
#         else:
#             print(" ", end="")
#     print()

# ----------Reverse Right-Angled Triangle /  Inverted Half Pyramid------------
#    1 2 3 4           i    j               j <= n + 1 - i
#  1 * * * *           1    1, 2, 3, 4      j <= 4 + 1 - 1
#  2 * * *             2    1, 2, 3         j <= 4 + 1 - 2
#  3 * *               3    1, 2            j <= 4 + 1 - 3
#  4 *                 4    1               j <= 4 + 1 - 4
# n = int(input("Enter the no. of rows: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if j <= n + 1 - i:
#             print("* ", end="")
#         else:
#             print(" ", end="")
#     print()

# -------------Half Diamond---------------
#    1 2 3 4           i    j               j <= i
#  1 *                 1    1               j <= 1
#  2 * *               2    1, 2            j <= 2
#  3 * * *             3    1, 2, 3         j <= 3
#  4 * * * *           4    1, 2, 3, 4      j <= 4
#  5 * * * * *         5    1, 2, 3, 4, 5   j <= 5
#  6 * * * *           1    1, 2, 3, 4      j <= 4 + 1 - 1
#  7 * * *             2    1, 2, 3         j <= 4 + 1 - 2
#  8 * *               3    1, 2            j <= 4 + 1 - 3
#  9 *                 4    1               j <= 4 + 1 - 4
# n = int(input("Enter the no. of rows: "))
# for i in range(0, n + 1):
#     for j in range(0, i + 1):
#         print("* ", end="")
#     print()
# for i in range(n, 0, -1):
#     for j in range(0, i):
#         print("* ", end="")
#     print()

# n = int(input("Enter the no. of rows: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if j <= i and j <= n + 1 -i:
#             print("*", end=" ")
#         else:
#             print(" ", end='')
#     print()


# ---------------------Pyramid----------------
#   1 2 3 4 5 6 7        i    j                     j >= n + 1 - i and j <= n - 1 + i
# 1       *              1    4                     j >= 4 + 1 - i and j <= 4 - 1 + 1
# 2     * * *            2    3, 4, 5               j >= 4 + 1 - 2 and j <= 4 - 1 + 2
# 3   * * * * *          3    2, 3, 4, 5, 6         j >= 4 + 1 - 3 and j <= 4 - 1 + 3
# 4 * * * * * * *        4    1, 2, 3, 4, 5, 6, 7   j >= 4 + 1 - 4 and j <= 4 - 1 + 4
# n = int(input("Enter the no. of rows: "))
# for i in range(1, n + 1):
#     for j in range(1, 2 * n):
#         if j >= n + 1 - i and j <= n - 1 + i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# n = int(input("Enter the no. of rows: "))
# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end="")
#     for j in range(2 * i + 1):
#         print("*", end="")
#     print()


# --------------------Triangle--------------------
#   1 2 3 4 5 6 7     i    j            j = n + 1 - i and j = n - 1 + i
# 1       *           1    4            j = 4 + 1 - 1 and j = 4 - 1 + 1
# 2     *   *         2    3, 5         j = 4 + 1 - 2 and j = 4 - 1 + 2
# 3   *   *   *       3    2, 4, 6      j = 4 + 1 - 3 and j = 4 - 1 + 3
# 4 *   *   *   *     4    1, 3, 5, 7   j = 4 + 1 - 4 and j = 4 - 1 + 4

n = int(input("Enter the no. of rows: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j >= n + 1 - i and j <= n - 1 + i:
            print("*", end=" ")
        else:
            print(" ", end="")
    print()


# -------------------------Pyramid-----------------------
# r = int(input("Enter the no. of rows: "))
# k = 2 * r - 2 # it us used for spaces
# for i in range(0, r):
#     for j in range(0, k):
#         print(end=" ")
#     k = k - 2
#     for j in range(0, 2 * i + 1):
#         print("*", end=" ")
#     print()

# -------------------------Reverse Pyramid-----------------------
# r = int(input("Enter the no. of rows: "))
# k = 2 * r - 2 # it us used for spaces
# for i in range(r, 0):
#     for j in range(k, 0):
#         print(end=" ")
#     k = k - 2
#     for j in range(2 * i + 1, 0):
#         print("*", end=" ")
#     print()