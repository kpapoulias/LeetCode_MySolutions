class Solution(object):
    def halfAdder(self, bit_a, bit_b):
        return (bit_a ^ bit_b, bit_a & bit_b )

    def fullAdder(self, bit_a, bit_b, c):
        s1, c1 = self.halfAdder(bit_a, bit_b)
        s2, c2 = self.halfAdder(s1, c)
        return (s2, c1 | c2)

    def addBinary(self, bits_a, bits_b):
        c = 0
        res = ""
        max_len = max(len(bits_a), len(bits_b))
        bits_a = bits_a.zfill(max_len)
        bits_b = bits_b.zfill(max_len)

        for i in range(len(bits_a)-1, -1, -1):
            s, c = self.fullAdder(int(bits_a[i]), int(bits_b[i]), c)
            res += str(s)
        if c == 1:
            res += str(c)
        return res[::-1]

    # Using inbuilt functions
    def addBinary1(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        s = bin(int(a,2) + int(b,2))
        return s[2:]