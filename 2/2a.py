import os

#data = [201,534,547,568,585,611,628,667,715,775,842,1104,1245,1466,1470,1471,1472,1475,1476,1477,1478,1482,1488,1492,1498,1499,1501,1502,1521,1524,1525,1529,1532,1533,1535,1545,1554,1560,1561,1563,1568,1571,1576,1584,1586,1590,1591,1592,1597,1598,1603,1604,1608,1614,1617,1619,1621,1623,1631,1633,1637,1641,1642,1644,1652,1653,1657,1661,1662,1667,1668,1672,1673,1676,1677,1679,1681,1682,1690,1691,1692,1695,1696,1697,1698,1702,1705,1707,1708,1710,1711,1713,1714,1716,1721,1727,1729,1730,1731,1738,1740,1747,1751,1754,1756,1760,1770,1771,1782,1785,1786,1794,1795,1798,1800,1801,1802,1809,1813,1817,1821,1822,1823,1825,1827,1830,1832,1834,1836,1841,1845,1846,1848,1849,1851,1854,1859,1861,1865,1872,1873,1875,1876,1878,1880,1883,1885,1886,1892,1893,1894,1895,1896,1897,1898,1899,1905,1910,1913,1916,1917,1921,1923,1925,1927,1931,1935,1936,1937,1941,1942,1943,1944,1947,1948,1949,1950,1955,1956,1957,1959,1960,1966,1968,1971,1972,1974,1977,1978,1980,1983,1985,1987,1993,1994,1996,1997,2000,2003,2006]
#data = [201,534,547,568,585,611,628,667,715,775,842,1104,1245,1466,1470,1471,1472,1475,1476,1477,1478,1482,1488,1492,1498,1499,1501,1502,1521,1524,1525,1529,1532,1533,1535,1545] #,1554,1560,1561,1563,1568,1571,1576,1584,1586,1590,1591,1592,1597,1598,1603,1604,1608,1614,1617,1619,1621,1623,1631,1633,1637,1641,1642,1644,1652,1653,1657,1661,1662,1667,1668,1672,1673,1676,1677,1679,1681,1682,1690,1691,1692,1695,1696,1697,1698,1702,1705,1707,1708,1710,1711,1713,1714,1716,1721,1727,1729,1730,1731,1738,1740,1747,1751,1754,1756,1760,1770,1771,1782,1785,1786,1794,1795,1798,1800,1801,1802,1809,1813,1817,1821,1822,1823,1825,1827,1830,1832,1834,1836,1841,1845,1846,1848,1849,1851,1854,1859,1861,1865,1872,1873,1875,1876,1878,1880,1883,1885,1886,1892,1893,1894,1895,1896,1897,1898,1899,1905,1910,1913,1916,1917,1921,1923,1925,1927,1931,1935,1936,1937,1941,1942,1943,1944,1947,1948,1949,1950,1955,1956,1957,1959,1960,1966,1968,1971,1972,1974,1977,1978,1980,1983,1985,1987,1993,1994,1996,1997,2000,2003,2006]
solved = False
x = 0
y = 0
z = 0

data = []

class Password:
    def __init__(self, line):
        v = line.split(" ")
        self.min = int(v[0].split("-")[0])
        self.max = int(v[0].split("-")[1])
        self.reqchr = v[1][0]
        self.pass_string = v[2]

        #print("Must have between {} and {} {}'s in {}".format(self.min, self.max,self.reqchr,self.pass_string))

    def test(self):
        count = self.pass_string.count(self.reqchr)
        if count >= self.min and count <= self.max:
            return 1
        else:
            return 0

total_valid = 0
total = 0
with open(os.path.join(os.getcwd(), "2020\\2\\input_2a.txt")) as f:
    for line in f:
        total+=1
        p = Password(line)
        total_valid += p.test()

print("{} are valid of {}".format(total_valid,total))
        

# data.sort()

# end = len(data)-1
# print ("End is {}".format(end))
# while solved == False:
#     res = data[x] + data[y] + data[z]
#     a = data[x]
#     b = data[y]
#     c = data[z]
#     #print("{},{},{}:{}+{}+{}={}".format(x,y,z,a,b,c,res))
#     if res == 2020:
#         solved = True
#         print("{},{},{}:{}+{}+{}=2020".format(x,y,z,a,b,c))
#         print("{}x{}x{}={}".format(a,b,c,a*b*c))

#     # else:
#     #     if x == end-2:
#     #         print("not found")
#     #         exit(1)
#     #     elif y == end-1:
#     #         x+=1
#     #         y= x+1
#     #         z= y+1
#     #     elif z == end:
#     #         y+=1
#     #         z=y+1
#     #     else:
#     #         z+=1

#     elif res > 2020:
#         print("{},{},{}:{}+{}+{}={}".format(x,y,z,a,b,c,res))
#         y+=1
#         z=y+1
#         print("next y")
#         print("({},{},{})".format(x,y,z))   
#     else:
#         print("{},{},{}:{}+{}+{}={}".format(x,y,z,a,b,c,res))
#         z+=1
#     if z == end:
#         if y == end-1:
#             x+=1
#             y=x+1
#             z=y+1
#             print("next x - b")
#         else:
#             y+=1
#             z=y
#             print("next y") 
    

