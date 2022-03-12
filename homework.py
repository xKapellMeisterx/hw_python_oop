class InfoMessage:
    """Базовый класс тренировки."""

    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float,
                 ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        """Информация о выполненной тренировке."""
        return (
            f"Тип тренировки: {self.training_type};"
            f" Длительность: {self.duration:.3f} ч.;"
            f" Дистанция: {self.distance:.3f} км;"
            f" Ср. скорость: {self.speed:.3f} км/ч;"
            f" Потрачено ккал: {self.calories:.3f}."
        )


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000
    HOUR_TO_MIN: int = 60
    training_type: str = ''

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.training_type,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories()
                           )


class Running(Training):
    """Тренировка: бег."""
    coeff_calorie_1: float = 0
    training_type: str = "Running"

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        self.coeff_calorie_1 = (18 * self.get_mean_speed() - 20) * self.weight / self.M_IN_KM \
                                * self.duration * self.HOUR_TO_MIN
        return self.coeff_calorie_1


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    coeff_calorie_2: float = 0
    training_type: str = "SportsWalking"

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float,
                 ) -> None:
        Training.__init__(self, action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        self.coeff_calorie_2 = (0.035 * self.weight
                                + (self.get_mean_speed() ** 2 // self.height) * 0.029 * self.weight) \
                                * self.duration * self.HOUR_TO_MIN
        return self.coeff_calorie_2


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = 1.38
    coeff_calorie_3: float = 0
    training_type: str = "Swimming"

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float,
                 ) -> None:
        Training.__init__(self, action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.length_pool * self.count_pool / self.M_IN_KM / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        self.coeff_calorie_3 = (self.get_mean_speed() + 1.1) * 2 * self.weight
        return self.coeff_calorie_3


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    class_data = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }

    return class_data[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""

    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
