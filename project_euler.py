import copy,math,time

class Solution(object):

    def problem_1(self):
        sum = 0
        for i in range(1000):
            if i % 3 ==0 or i % 5 ==0:
                sum += i
        return sum

    def problem_2(self):
        sum = 0
        fib = [1,2]
        x = 0
        while x<4000000:
            x = fib[-1]+fib[-2]
            fib.append(copy.deepcopy(x))
        for i in fib:
            sum += i if i%2 ==0 else 0
        return sum

    def problem_3(self):
        x = 600851475143
        rx = int(math.sqrt(x))
        print(rx)
        prime = [2]
        factor = []
        for i in range(2,100000):
            for j in prime:
                if i%j == 0:
                    break
            else:
                prime.append(i)
        for i in prime:
            if x%i == 0:
                factor.append(i)
        return factor

    def problem_4(self):
        m = 0
        for i in range(100,1000):
            for j in range(i,1000):
                x = i*j
                if is_palindrome(x):
                    m = max(m,int(x))
        return m

    def problem_5(self):
        eff = []
        li = [x for x in range(1,21)]
        i = 2
        while not sum(li)==20:
            ch = 0
            for x in range(len(li)):
                if li[x]%i==0 and li[x] != 1:
                    li[x] = int(li[x]/i)
                    ch = 1
            if ch == 0:
                i +=1
            else:
                eff.append(i)
        mul = 1
        for item in eff:
            mul *= item
        return mul

    def problem_6(self):
        a = sum([x**2 for x in range(1,101)])
        b = sum([x for x in range(1,101)])
        return b**2 - a

    def problem_7(self):
        prime = [2]
        i = 2
        while len(prime) < 10001:

            for j in prime:
                if i%j == 0:
                    break
            else:
                prime.append(i)
            i += 1
        return prime[-1]

    def problem_8(self):
        s= "73167176531330624919225119674426574742355349194934" \
           "96983520312774506326239578318016984801869478851843" \
           "85861560789112949495459501737958331952853208805511" \
           "12540698747158523863050715693290963295227443043557" \
           "66896648950445244523161731856403098711121722383113" \
           "62229893423380308135336276614282806444486645238749" \
           "30358907296290491560440772390713810515859307960866" \
           "70172427121883998797908792274921901699720888093776" \
           "65727333001053367881220235421809751254540594752243" \
           "52584907711670556013604839586446706324415722155397" \
           "53697817977846174064955149290862569321978468622482" \
           "83972241375657056057490261407972968652414535100474" \
           "82166370484403199890008895243450658541227588666881" \
           "16427171479924442928230863465674813919123162824586" \
           "17866458359124566529476545682848912883142607690042" \
           "24219022671055626321111109370544217506941658960408" \
           "07198403850962455444362981230987879927244284909188" \
           "84580156166097919133875499200524063689912560717606" \
           "05886116467109405077541002256983155200055935729725" \
           "71636269561882670428252483600823257530420752963450"
        st_pos = 0
        m = 1
        while st_pos < 1000-13:
            mul = 1
            for i in range(13):
                mul *= int(s[st_pos + i])
                if s[st_pos+i] == '0':
                    st_pos = st_pos + i+1
                    break
            if not mul == 0:
                m =max(m,mul)
                st_pos+=1
        return m

    def problem_9(self):
        for a in range(1,999):
            for b in range(a+1,1001):
                c = 1000-a-b
                if a**2 + b**2 == c**2:
                    return a*b*c

    def problem_10(self):
        #return sum([x for x in range(2,2000000) if is_prime(x)])
        n= 20000000
        sieve = [True]*n
        for i in range(3, int(n**0.5)+1, 2):
            if sieve[i]:
                sieve[i**2::2*i]=[False]*int((n-i*i-1)/(2*i)+1)
                # sieve[i**2::i]=[False]*int((n-i*i-1)/(i)+1)
        return sum([2] + [i for i in range(3, n, 2) if sieve[i]])

    def problem_11(self):
        s = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 " \
            "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 " \
            "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 " \
            "52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 " \
            "22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 " \
            "24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 " \
            "32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 " \
            "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 " \
            "24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 " \
            "21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 " \
            "78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 " \
            "16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 " \
            "86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 " \
            "19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 " \
            "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 " \
            "88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 " \
            "04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 " \
            "20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 " \
            "20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 " \
            "01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48 "
        s= s.split(' ')
        s_li = []
        for i in range(20):
            s_s = []
            for j in range(20):
                s_s.append(int(s[i*20+j]))
            s_li.append(s_s)
        print(s_li)
        mv = 0
        i = 0
        j = 0
        # row
        for i in range(20):
            for j in range(16):
                pos = [None]*4
                mul = 1
                for k in range(4):
                    pos[k] = s_li[i][j+k]
                    mul *= pos[k]
                print(pos)
                mv = max(mv,mul)
        # col
        for i in range(16):
            for j in range(20):
                pos = [None] * 4
                mul = 1
                for k in range(4):
                    pos[k] = s_li[i+k][j]
                    mul *= pos[k]
                print(pos)
                mv = max(mv, mul)
        # \
        for i in range(16):
            for j in range(16):
                pos = [None] * 4
                mul = 1
                for k in range(4):
                    pos[k] = s_li[i + k][j + k]
                    mul *= pos[k]
                print(pos)
                mv = max(mv, mul)
        # /
        for i in range(16):
            for j in range(3,20):
                pos = [None] * 4
                mul = 1
                for k in range(4):
                    pos[k] = s_li[i+k][j-k]
                    mul *= pos[k]
                print(pos)
                mv = max(mv, mul)
        return mv

    def problem_12(self):
        n = 1
        while True:
            tri_num = sum([x for x in range(1,n+1)])
            # divs = []
            count = 0
            for i in range(1,int(math.sqrt(tri_num))+1):
                if tri_num%i == 0:
                    # divs.append(i)
                    count += 1
            # if len(divs)>=250:
            #     return tri_num
            if count >= 250:
                return tri_num
            n += 1

    def problem_13(self):
        s = []
        with open("problem_12.txt",'r') as f:
            for line in f:
                s.append(line.replace('\n',''))
        res = []
        carry = 0
        for pos in range(50):
            carry, su = divmod(sum([int(num[-(pos+1)]) for num in s])+carry, 10)
            res.append(str(su))
        carry, su = divmod(carry, 10)
        res.append(str(su))
        res.append(str(carry))
        return ''.join(res[:-11:-1])

    def problem_14(self):
        n = 1000000
        mc = 0
        ms = 0
        for start in range(3,n+1):
            x = start
            count = 0
            while x != 1:
                if x %2 ==0:
                    x /= 2
                else:
                    x = 3*x +1
                count += 1
            if count > mc:
                mc = count
                ms = start
        return ms

    def problem_15(self):
        tri = [[1],[1,1]]
        while len(tri)<21:
            new_line = []
            for i in range(len(tri[-1])-1):
                new_line.append(tri[-1][i]+tri[-1][i+1])
            tri.append([1]+new_line+[1])

        print(tri)
        return sum([x**2 for x in tri[-1]])

    def problem_16(self):
        return sum([int(x) for x in str(2**1000)])

    def problem_17(self):
        letters = [0]*1001
        result = [0] * 1001
        buffer = ''
        with open('problem_17.txt','r') as f:
            s = f.readline()
            while not s == '' :
                buffer += s
                s = f.readline()
        buffer = buffer.replace('\n', ' ')
        buffer = buffer.split(' ')
        buffer = [x for x in buffer if x != '']
        for i in range(0,len(buffer)-1,2):
            letters[int(buffer[i])] = len(buffer[i+1])
        for i in range(1,len(result)):
            s = int(i%10)
            t = int(i/10)%10
            h = int(i/100)%10
            if t>=2:
                result[i] = letters[h]+letters[t*10]+letters[s]
            if t<2:
                result[i] = letters[h]+letters[i%100]
            if i%100 != 0 and i > 100:
                result[i] += 3 +letters[100]
            if 1000>i > 100 and i%100 ==0:
                result[i] += letters[100]
            # 1000 and 100 is not include
        return sum(result)+letters[1]+letters[1000]+letters[100]

    def problem_18(self):
        tri = []
        with open('problem_18.txt','r') as f:
            s= f.readline()
            while s:
                tri.append(s.replace('\n','').split(' '))
                s = f.readline()
        while not len(tri) < 2:
            for i in range(len(tri[-2])):
                if int(tri[-2][i])+int(int(tri[-1][i])) > int(tri[-2][i])+int(int(tri[-1][i+1])):
                    tri[-2][i] = int(tri[-2][i]) + int(int(tri[-1][i]))
                else:
                    tri[-2][i] = int(tri[-2][i]) + int(int(tri[-1][i+1]))
            tri.pop(-1)
        return tri

    def problem_67(self):
        tri = []
        with open('problem_67.txt','r') as f:
            s= f.readline()
            while s:
                tri.append(s.replace('\n','').split(' '))
                s = f.readline()
        while not len(tri) < 2:
            for i in range(len(tri[-2])):
                if int(tri[-2][i])+int(int(tri[-1][i])) > int(tri[-2][i])+int(int(tri[-1][i+1])):
                    tri[-2][i] = int(tri[-2][i]) + int(int(tri[-1][i]))
                else:
                    tri[-2][i] = int(tri[-2][i]) + int(int(tri[-1][i+1]))
            tri.pop(-1)
        return tri

    def problem(self):




def is_prime(x):
    if x <=1 :
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            return False
    return True


def is_palindrome(x):
    s = str(x)
    for i in range(len(s)):
        if s[i] != s[-(i+1)]:
            return False
    return True



if __name__ == '__main__':
    s = Solution()
    t= time.time()
    print('The answer is: %s'%s.problem())
    print('Time used: %f'%(time.time()-t))