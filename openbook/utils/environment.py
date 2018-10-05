class InvalidEnvironmentValueError(AttributeError):
    pass


class EmptyEnvironmentValueError(AttributeError):
    pass


class EnvironmentChecker:
    PRODUCTION_VALUE = 'production'
    ACCEPTANCE_VALUE = 'acceptance'
    DEVELOPMENT_VALUE = 'development'

    ALLOWED_ENVIRONMENTS = [
        PRODUCTION_VALUE,
        DEVELOPMENT_VALUE,
        ACCEPTANCE_VALUE,
    ]

    def __init__(self, environment_value):
        if not self.is_valid_environment_value(environment_value):
            raise InvalidEnvironmentValueError

        self.environment_value = environment_value

    def is_production(self):
        return self.environment_value == self.PRODUCTION_VALUE

    def is_development(self):
        return self.environment_value == self.DEVELOPMENT_VALUE

    def is_acceptance(self):
        return self.environment_value == self.ACCEPTANCE_VALUE

    def is_debug(self):
        return self.is_development() or self.is_acceptance()

    def is_valid_environment_value(self, environment_value):
        return environment_value in self.ALLOWED_ENVIRONMENTS