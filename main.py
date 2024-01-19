from typing import Dict, List

students = {
    'alex': {'math': 91, 'economics': 98},
    'john': {'math': 50, 'economics': 59},
    'elena': {'math': 100, 'economics': 99},
    'pavel': {'math': 76, 'economics': 90},
    'nastya': {'math': 95, 'economics': 100},
    'oleg': {'math': 86, 'economics': 89},
    'peter': {'math': 60, 'economics': 75},
    'yana': {'math': 87, 'economics': 90},
    'magamed': {'math': 52, 'economics': 68},
    'maxim': {'math': 60, 'economics': 57},
}


def get_high_result(container: Dict[str, dict]) -> List[str]:
    excellent_assessment = []
    for key in container:
        if container[key]['math'] >= 86:
            excellent_assessment.append(key)
    return excellent_assessment


print(get_high_result(students))
