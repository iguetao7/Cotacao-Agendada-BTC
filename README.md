# Cotação Agendada de Bitcoin (BTC)

## Visão Geral
Automação desenvolvida para **consultar e enviar cotações de Bitcoin (BTC) de forma agendada**, utilizando integrações com APIs externas e canais de comunicação automatizados. O projeto foi criado para fornecer informações financeiras atualizadas sem necessidade de consulta manual.

## Problema
Acompanhar a cotação de criptomoedas manualmente exige consultas frequentes a plataformas externas, o que consome tempo e pode gerar perda de informações importantes quando não há monitoramento contínuo.

## Solução
Este projeto implementa uma automação que:
- Consulta periodicamente a cotação do Bitcoin por meio de API  
- Processa e organiza os dados obtidos  
- Envia a cotação automaticamente em horários definidos  

A solução elimina a necessidade de acompanhamento manual e garante acesso rápido e recorrente às informações de mercado.

## Tecnologias Utilizadas
- Python  
- APIs de cotação de criptomoedas  
- Requests  
- Automação de tarefas agendadas  

## Como Funciona
1. O script realiza requisições a uma API de cotação de criptomoedas.  
2. Os dados retornados são processados e formatados.  
3. A cotação é enviada automaticamente conforme o agendamento definido.  
4. O processo pode ser executado de forma recorrente, sem intervenção manual.

## Execução
Instale as dependências:
```bash
pip install -r requirements.txt
