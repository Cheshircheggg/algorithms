class Member:

    def __init__(self, name, points, penalty):
        self.name = name
        self.points = points
        self.penalty = penalty

    def __lt__(self, other: 'Member'):
        return ((-self.points, self.penalty, self.name) <
                (-other.points, other.penalty, other.name))

    def __str__(self):
        return self.name


def quick_sort(arr, zero_position, last_position):
    if zero_position >= last_position:
        return -1

    left, right = zero_position, last_position
    pivot = arr[zero_position]

    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    quick_sort(arr, zero_position, right)
    quick_sort(arr, left, last_position)


if __name__ == '__main__':
    members_count = int(input())
    members = []
    for _ in range(members_count):
        name, score, penalty = input().split()
        members.append(Member(name, int(score), int(penalty)))

    quick_sort(members, 0, members_count - 1)
    print(*members, sep='\n')
