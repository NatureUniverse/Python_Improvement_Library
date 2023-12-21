class valuesetter:
    def __init__(self):
        self.variables = {}

    def run(self, code):
        lines = code.split('\n')
        for line in lines:
            self.interpret_line(line)

    def interpret_line(self, line):
        tokens = line.split()
        if tokens:
            if tokens[0] == 'print' and len(tokens) >= 2:
                self.print_value(tokens[1])
            elif tokens[0] == 'dec' and len(tokens) >= 4:  #모든 data type -> dec설정
                self.set_variable(tokens[1], tokens[3])
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
            self.variables[variable_name] = int(value)  # 정수로 변환 시도
        except ValueError:
            try:
                self.variables[variable_name] = float(value)  # 실수로 변환 시도
            except ValueError:
                try:
                    self.variables[variable_name] = complex(value)  # 복소수로 변환 시도
                except ValueError:
                    try:
                        self.variables[variable_name] = str(value)  # 문자열(유니코드)로 변환 시도
                    except ValueError:
                        try:
                            self.variables[variable_name] = bytes(value)  # 문자열(0~255범위의 문자)로 변환 시도
                        except ValueError:
                            try:
                                self.variables[variable_name] = list(value)  # 자료로 변환 시도(이하 4개)
                            except ValueError:
                                try:
                                    self.variables[variable_name] = tuple(value)
                                except ValueError:
                                    try:
                                        self.variables[variable_name] = dict(value)
                                    except ValueError:
                                        try:
                                            self.variables[variable_name] = set(value)
                                        except ValueError:
                                            self.variables[variable_name] = bool(value)  # 참 거짓 변환 시도
