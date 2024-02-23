class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        devices_per_row: List[int] = []

        for i in range(len(bank)):
            devices_in_row: int = 0
            for j in range(len(bank[i])):
                if bank[i][j] == '1':
                    devices_in_row += 1
            devices_per_row.append(devices_in_row)

        temp: List[int] = []
        for i in range(len(devices_per_row)):
            if devices_per_row[i] != 0:
                temp.append(devices_per_row[i])
        devices_per_row = temp




        total_lazers: int = 0
        print(devices_per_row)
        for i in range(len(devices_per_row) - 1):
            total_lazers += devices_per_row[i] * devices_per_row[i + 1]
        return total_lazers


