from dataclasses import dataclass, asdict


@dataclass
class InfoMessage:
    """Информация о тренировке."""

    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float
    MESSAGE: str = ('Тип тренировки: {training_type}; '
                    'Длительность: {duration:.3f} ч.; '
                    'Дистанция: {distance:.3f} км; '
                    'Ср. скорость: {speed:.3f} км/ч; '
                    'Потрачено ккал: {calories:.3f}.')

    def get_message(self):
        """Наполнение информации о тренировке в MESSAGE."""
        return self.MESSAGE.format(**asdict(self))


class Training:
    """Базовый класс тренировки."""

    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000
    HOUR_TO_MIN: int = 60

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
        raise NotImplementedError(
            'Определите \"def get_spent_calories\" в наследнике')

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.__class__.__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories()
                           )


class Running(Training):
    """Тренировка: бег."""

    coeff_calorie_1: int = 18
    coeff_calorie_2: int = 20

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        running_calories = (
            (self.coeff_calorie_1 * self.get_mean_speed()
             - self.coeff_calorie_2)
            * self.weight / self.M_IN_KM
            * self.duration * self.HOUR_TO_MIN)
        return running_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    coeff_calorie_1: float = 0.035
    coeff_calorie_2: int = 2
    coeff_calorie_3: float = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float,
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        sportswalking_calories = (
            (self.coeff_calorie_1 * self.weight
             + (self.get_mean_speed() ** self.coeff_calorie_2 // self.height)
             * self.coeff_calorie_3 * self.weight) * self.duration
            * self.HOUR_TO_MIN)
        return sportswalking_calories


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP: float = 1.38
    coeff_calorie_1: float = 1.1
    coeff_calorie_2: int = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float,
                 ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return (
            self.length_pool * self.count_pool
            / self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        swimming_calories = (
            (self.get_mean_speed() + self.coeff_calorie_1)
            * self.coeff_calorie_2 * self.weight)
        return swimming_calories


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    class_data: dict[str, Type[Swimming | Running | SportsWalking]] = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }

    if workout_type not in class_data:
        raise KeyError('Неизвестный тип тренировки')
    return class_data[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    print(training.show_training_info().get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
