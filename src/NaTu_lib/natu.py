class _SimpleInterpreter:
    def __init__(self):
        self.variables = {}

    def run(self, code):
        lines = code.split('\n')
        for line in lines:
            self.interpret_line(line)

    def interpret_line(self, line):
        tokens = line.split()
        if tokens:
            if tokens[0] == 'prints' and len(tokens) >= 2:
                self.print_value(tokens[1])
            elif tokens[0] == 'dec' and len(tokens) >= 4:
                self.set_variable(tokens[1], ' '.join(tokens[3:]))
            elif len(tokens) >= 4 and tokens[1] == '=':
                result_var = tokens[0]
                expression = ' '.join(tokens[2:])
                self.evaluate_expression(result_var, expression)

    def print_value(self, variable_name):
        if variable_name in self.variables:
            print(self.variables[variable_name])
        else:
            print(f"Error: Variable '{variable_name}' not found.")

    def set_variable(self, variable_name, value):
        try:
            # 사용자가 dec 키워드를 사용하면 자동으로 데이터 타입을 인식하여 설정
            self.variables[variable_name] = self.auto_detect_data_type(value)
        except ValueError as e:
            print(f"Error setting variable '{variable_name}': {str(e)}")

    def auto_detect_data_type(self, value):
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                try:
                    return complex(value)
                except ValueError:
                    try:
                        return str(value)
                    except ValueError:
                        try:
                            return bytes(value, encoding='utf-8')
                        except ValueError:
                            try:
                                return list(value)
                            except ValueError:
                                try:
                                    return tuple(value)
                                except ValueError:
                                    try:
                                        return dict(value)
                                    except ValueError:
                                        try:
                                            return set(value)
                                        except ValueError:
                                            return bool(value)

# Singleton pattern을 사용하여 한 번만 인스턴스 생성
natu_instance = _SimpleInterpreter()

# dec 키워드를 사용하여 변수를 설정하는 함수
def dec(variable_name, value):
    natu_instance.set_variable(variable_name, value)

# print 키워드를 사용하여 변수를 출력하는 함수
def prints(variable_name):
    natu_instance.print_value(variable_name)
