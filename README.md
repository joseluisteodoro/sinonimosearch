# 📚 Buscador de Sinônimos

**Buscador de Sinônimos** é um pacote Python criado como parte de um desafio da [DIO](https://www.dio.me/), com o objetivo de buscar e exibir sinônimos para palavras da língua portuguesa diretamente no terminal.

## 🚀 Funcionalidades

- Recebe uma palavra como entrada
- Realiza consulta online no site [sinonimos.com.br](https://www.sinonimos.com.br)
- Exibe os sinônimos encontrados com formatação tabulada e visual limpa

## 📦 Instalação

Use o [pip](https://pip.pypa.io/en/stable/) para instalar o pacote:

```bash
pip install sinonimosearch
```

## 🧪 Exemplo de uso

```python
from sinonimosearch import buscarsinonimo

buscarsinonimo.buscarporpalavra("feliz")
```

🔹 A função irá imprimir os sinônimos diretamente no terminal com o seguinte estilo:

```
🔎 Sinônimos para: 'feliz'
----------------------------------------
    • alegre
    • contente
    • animado
    ...
----------------------------------------
✅ Total encontrados: 25
```

## 👤 Autor

**José Luís Teodoro**  
GitHub: [@joseluisteodoro](https://github.com/joseluisteodoro)

## 📄 Licença

Distribuído sob a licença [MIT](https://choosealicense.com/licenses/mit/).  
Sinta-se livre para usar, modificar e compartilhar!
