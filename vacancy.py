class Vacancy:
    def __init__(self, job, exp, sex, edu, age_min, age_max, lang, salary, social, prob):
        self.position = job  # Название должности
        self.experience = exp  # Требуемый стаж работы (лет)
        self.gender = sex  # Предпочтительный пол
        self.education = edu  # Требуемое образование
        self.min_age = age_min  # Минимальный возраст
        self.max_age = age_max  # Максимальный возраст
        self.languages = lang  # Знание иностранных языков
        self.min_salary = salary  # Минимальный оклад (руб.)
        self.social_package = social  # Наличие соцпакета (True/False)
        self.probation_period = prob  # Испытательный срок (мес.)