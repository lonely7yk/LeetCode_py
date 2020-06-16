"""
Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, 
each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. 
The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 
is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case 
characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 
address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive 
colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 
02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the input string.

Example 1:
Input: "172.16.254.1"

Output: "IPv4"

Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:
Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

Output: "IPv6"

Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:
Input: "256.256.256.256"

Output: "Neither"

Explanation: This is neither a IPv4 address nor a IPv6 address.
"""

class Solution:
    def validIPAddress(self, IP: str) -> str:
        if '.' in IP:
            nums = IP.split('.')
            if len(nums) != 4: return 'Neither'

            for num in nums:
                # 以 0 开头
                if len(num) > 1 and num[0] == '0':
                    return 'Neither'

                # 没有数字
                if len(num) == 0:
                    return 'Neither'

                # 有数字不在 0-9 范围内
                for c in num:
                    if c not in '0123456789':
                        return 'Neither'

                if int(num) < 0 or int(num) > 255:
                    return 'Neither'

            return 'IPv4'
        elif ':' in IP:
            nums = IP.split(':')
            if len(nums) != 8: return 'Neither'

            for num in nums:
                # 长度必须在 1-4 范围内
                if len(num) == 0 or len(num) > 4: return 'Neither'

                for c in num:
                    if c not in '0123456789abcdefABCDEF':
                        return 'Neither'

            return 'IPv6'
        else:
            return 'Neither'


# IP = '172.16.254.1'
# IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
# IP = "256.256.256.256"

# IP = "2001:db8:85a3:0::8a2E:0370:7334"
IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"

res = Solution().validIPAddress(IP)
print(res)
