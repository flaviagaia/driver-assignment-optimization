# driver-assignment-optimization

## Português

`driver-assignment-optimization` é um projeto inspirado em uma pergunta típica de DoorDash: **como construir uma lógica de atribuição de motoristas a pedidos**.

O projeto simula candidatos de matching por pedido e escolhe o melhor entregador usando um score que combina:

- probabilidade de aceitação;
- distância até o pickup;
- atraso estimado no pickup;
- utilização do entregador.

## O que o projeto faz

1. gera candidatos sintéticos de order-driver matching;
2. calcula um score por candidato;
3. escolhe o melhor candidato por pedido;
4. resume a qualidade da política de atribuição.

## Objetivo da otimização

- maximizar aceitação;
- controlar atraso de pickup;
- evitar distância excessiva;
- manter utilização saudável.

## Técnicas e bibliotecas

- heuristic scoring
- greedy assignment
- `Python`
- `csv`
- `json`
- `pathlib`
- `unittest`

## Como executar

```bash
python3 main.py
python3 -m unittest discover -s tests -v
python3 -m py_compile main.py src/data_factory.py src/modeling.py tests/test_project.py
```

## Como defender em entrevista

> Para driver assignment, eu começaria com uma política de ranking simples e auditável, combinando aceitação esperada, distância ao pickup, delay estimado e utilização. Esse projeto mostra exatamente esse primeiro passo antes de evoluir para um matching ou optimization layer mais sofisticado.
