class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Encuentra los índices de dos números adyacentes que sumen el target.
        
        Complejidad Temporal: O(n) - Se recorre el arreglo una sola vez.
        Complejidad Espacial: O(1) - No se requiere memoria adicional.
        """
        # Recorremos hasta el penúltimo elemento para evitar un IndexError
        for i in range(len(nums) - 1):
            if nums[i] + nums[i+1] == target:
                return [i, i+1]
        
        return []