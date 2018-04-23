def feibo(x):
    if x ==1:
        return [0]
    if x ==2:
        return [0,1]
    if x>2:
        result = [0,1]
        for i in range(x-2):
            result.append(result[-2]+result[-1])
        return result

if __name__ == '__main__':
    nums = int(input('Please enter a number: '))
    print(feibo(nums))
    
