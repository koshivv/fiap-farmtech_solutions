# Carrega o pacote para lidar com a API REST
library(jsonlite)

cat("\n========================================\n")
cat("🌤️  FARMTECH SOLUTIONS - CLIMA AGORA 🌤️\n")
cat("========================================\n")

# 1. Solicitando as coordenadas ao usuário
cat("Para verificar o clima exato do seu talhão, informe as coordenadas.\n")
cat("(Dica: Use ponto para decimais, ex: -21.1775)\n")

# Exemplo de valores de São Paulo (Praça da Sé) Latitude(-23.5505) e Longitude(-46.6333)
lat_usuario <- readline(prompt="Digite a latitude: ")
lon_usuario <- readline(prompt="Digite a longitude: ")

cat("\nConectando aos satélites meteorológicos...\n\n")

# 2. Construindo a URL dinâmica com as variáveis informadas
url_dinamica <- paste0("https://api.open-meteo.com/v1/forecast?latitude=", lat_usuario, "&longitude=", lon_usuario, "&current_weather=true")

# 3. Consumindo a API e convertendo o JSON para uma Lista no R
dados_clima <- fromJSON(url_dinamica)

# 4. Extraindo os dados específicos da lista usando o cifrão ($)
temperatura <- dados_clima$current_weather$temperature
velocidade_vento <- dados_clima$current_weather$windspeed
hora_atualizacao <- dados_clima$current_weather$time

# 5. Exibindo os resultados em texto simples no terminal
cat("📍 Coordenadas analisadas: Lat", lat_usuario, "| Lon", lon_usuario, "\n")
cat("🕒 Última atualização:", hora_atualizacao, "\n")
cat("🌡️  Temperatura Atual:", temperatura, "°C\n")
cat("💨 Velocidade do Vento:", velocidade_vento, "km/h\n")
cat("----------------------------------------\n")

# 6. Lógica de Negócio (Alerta de Pulverização)
if (velocidade_vento > 10) {
  cat("⚠️ ALERTA AGRONÔMICO: Vento muito forte!\n")
  cat("Risco de deriva elevado. NÃO inicie a pulverização dos defensivos agora.\n")
} else if (temperatura > 30) {
  cat("⚠️ ALERTA AGRONÔMICO: Temperatura muito alta!\n")
  cat("Risco de evaporação rápida da calda. Aguarde um horário mais fresco para pulverizar.\n")
} else {
  cat("✅ CONDIÇÕES IDEAIS: Clima favorável!\n")
  cat("Os tratores estão liberados para iniciar o manejo de pulverização.\n")
}
cat("========================================\n")

