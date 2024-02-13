'''
Реализуйте класс Config, который соответствует шаблону синглтон и 
описывает конфигурационный объект с фиксированными параметрами. 
При создании экземпляра класс не должен принимать никаких аргументов.

При первом вызове класса Config должен создаваться и 
возвращаться экземпляр этого класса, а при последующих вызовах должен 
возвращаться экземпляр, созданный при первом вызове.

Экземпляр класса Config должен иметь четыре атрибута:

program_name — атрибут со строковым значением GenerationPy
environment — атрибут со строковым значением release
loglevel — атрибут со строковым значением verbose
version — атрибут со строковым значением 1.0.0 
'''

class Config:
    _instance = None

    def __new__(cls,program_name='GenerationPy', environment='release',loglevel='verbose', version='1.0.0' ):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        cls._instance.program_name = program_name
        cls._instance.environment = environment
        cls._instance.loglevel = loglevel
        cls._instance.version = version
        return cls._instance
    


config = Config()

print(config.program_name)
print(config.environment)
print(config.loglevel)
print(config.version)