from decimal import Decimal


class FanDuel:
    @staticmethod
    def calculate_position_score(position: str) -> Decimal:
        if position.startswith("T"):
            p = position[1:]
        else:
            p = position

        try:
            position_num = int(p)
        except ValueError:
            return Decimal("0")

        match position_num:
            case 1:
                return Decimal("30")
            case 2:
                return Decimal("20")
            case 3:
                return Decimal("18")
            case 4:
                return Decimal("16")
            case 5:
                return Decimal("14")
            case 6:
                return Decimal("12")
            case 7:
                return Decimal("10")
            case 8:
                return Decimal("8")
            case 9:
                return Decimal("7")
            case 10:
                return Decimal("6")
            case position_num if position_num in list(range(11, 16)):
                return Decimal("5")
            case position_num if position_num in list(range(16, 21)):
                return Decimal("4")
            case position_num if position_num in list(range(21, 26)):
                return Decimal("3")
            case position_num if position_num in list(range(26, 31)):
                return Decimal("2")
            case position_num if position_num in list(range(31, 41)):
                return Decimal("1")
            case _:
                return Decimal("0")

    @staticmethod
    def calculate_bogey_free_round_score(bogey_count: int) -> Decimal:
        return Decimal("5") if bogey_count == 0 else Decimal("0")

    @staticmethod
    def calculate_birdie_or_better_score(birdie_or_better_count: int) -> Decimal:
        return Decimal("4") if birdie_or_better_count >= 5 else Decimal("0")

    @staticmethod
    def calculate_hole_result_score(hole_result: str) -> Decimal:
        match hole_result:
            case "EAGLE_OR_BETTER":
                return Decimal("7")
            case "BIRDIE":
                return Decimal("3.1")
            case "PAR":
                return Decimal("0.5")
            case "BOGEY":
                return Decimal("-1")
            case "DOUBLE_BOGEY_OR_WORSE":
                return Decimal("-3")
            case _:
                raise Exception(f"Unexpected hole result: {hole_result}")

    @staticmethod
    def calculate_streak_score(hole_result: str, previous_hole_result: str) -> Decimal:
        if hole_result in ["BIRDIE", "EAGLE_OR_BETTER"] and previous_hole_result in [
            "BIRDIE",
            "EAGLE_OR_BETTER",
        ]:
            return Decimal("0.6")
        else:
            return Decimal("0")

    @staticmethod
    def calculate_bounce_back_score(
        hole_result: str, previous_hole_result: str
    ) -> Decimal:
        if hole_result in ["BIRDIE", "EAGLE_OR_BETTER"] and previous_hole_result in [
            "BOGEY",
            "DOUBLE_BOGEY_OR_WORSE",
        ]:
            return Decimal("0.3")
        else:
            return Decimal("0")
