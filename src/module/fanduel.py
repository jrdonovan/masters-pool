class FanDuel:
    @staticmethod
    def calculate_position_score(position: str) -> int:
        if position.startswith("T"):
            position_num = position[1:]
        else:
            position_num = position

        match position_num:
            case 1:
                return 30
            case 2:
                return 20
            case 3:
                return 18
            case 4:
                return 16
            case 5:
                return 14
            case 6:
                return 12
            case 7:
                return 10
            case 8:
                return 8
            case 9:
                return 7
            case 10:
                return 6
            case position_num if position_num in list(range(11, 16)):
                return 5
            case position_num if position_num in list(range(16, 21)):
                return 4
            case position_num if position_num in list(range(21, 26)):
                return 3
            case position_num if position_num in list(range(26, 31)):
                return 2
            case position_num if position_num in list(range(31, 41)):
                return 1
            case _:
                return 0

    @staticmethod
    def calculate_bogey_free_round_score(bogey_count: int) -> int:
        return 5 if bogey_count == 0 else 0

    @staticmethod
    def calculate_birdie_or_better_score(birdie_or_better_count: int) -> int:
        return 4 if birdie_or_better_count >= 5 else 0

    @staticmethod
    def calculate_hole_result_score(hole_result: str) -> float:
        match hole_result:
            case "EAGLE_OR_BETTER":
                return 7
            case "BIRDIE":
                return 3.1
            case "PAR":
                return 0.5
            case "BOGEY":
                return -1
            case "DOUBLE_BOGEY_OR_WORSE":
                return -3
            case _:
                raise Exception(f"Unexpected hole result: {hole_result}")
