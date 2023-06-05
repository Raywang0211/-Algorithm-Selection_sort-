### 簡介：

初等排序法的一種，用來將數字由小到大或是由大到小排列。

## 執行過程：

挑出數列中的最小值並且與第一位交換，接著在從剩餘的數中在挑選最小值與第二位交換，重複此動作直到剩餘數只剩下1為止

### 舉例：

1. 9>5>3>1>2：1 - 9 交換位置（1>5>3>9>2）確定剩餘數列中最小值為1且固定了
2. 1>5>3>9>2：2 - 5 交換位置（1>2>3>9>5）確定剩餘數列中最小值為2且將位置固定了
3. 1>2>3>9>5：3  不須交換位置 （1>2>3>9>5）
4. 1>2>3>9>5：5 - 9 交換位置 （1>2>3>5>9）
5. 剩餘數列數量於 1 結束交換

## 注意：

## 複雜度：

時間複雜度

最差：O(n^2)

最佳：O(n) 已經排序好了

平均：

空間複雜度

最差：O(n)

## 程式：

```python
def selection_sort(seq,order=1):
    if order==1:
        for i in range(len(seq)-1):
            id_new = seq.index(min(seq[i:]))
            seq[i],seq[id_new] = seq[id_new],seq[i]
    else:
        for i in range(len(seq)-1):
            id_new = seq.index(max(seq[i:]))
            seq[i],seq[id_new] = seq[id_new],seq[i]

    return seq

print(selection_sort([4,8,9,1,3,2],0))
```