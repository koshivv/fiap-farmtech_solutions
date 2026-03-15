# Leitura do arquivo dados_farmtech.csv
df <- read.csv("dados_farmtech.csv", header = TRUE, sep = ",")

# Exibe as primeiras 5 linhas do novo df
head(df)

# Criação dos df_cafe e df_soja
df_cafe <- df[df$Cultura == "café", ]
print(df_cafe)

df_soja <- df[df$Cultura == "soja", ]
print(df_soja)

# Cálculo da média da produtividade (Produtividade_Sacas_ha) por cultura

library(dplyr) # Utilizando a função mutate() para alterar o datatype de algumas colunas para int

cafe_prod_media <- df_cafe %>% mutate(
  Produtividade_Sacas_ha = as.numeric(Produtividade_Sacas_ha)) %>% 
  summarise(prod_media = mean(Produtividade_Sacas_ha, na.rm = TRUE)) %>%
  pull(prod_media)

soja_prod_media <- df_soja %>% mutate(
  Produtividade_Sacas_ha = as.numeric(Produtividade_Sacas_ha)) %>% 
  summarise(prod_media = mean(Produtividade_Sacas_ha, na.rm = TRUE)) %>%
  pull(prod_media)

# Criação do df_final que irá armazenar todos os valores calculados

df_final <- data.frame(
    cultura = c("café", "soja")
  , prod_media = round(c(cafe_prod_media, soja_prod_media), 1)
)

# Cálculo do desvio padrão da produtividade de cada cultura
cafe_prod_desvpad <- df_cafe %>% mutate(
  Produtividade_Sacas_ha = as.numeric(Produtividade_Sacas_ha)) %>%
  summarise(desvpad = sd(Produtividade_Sacas_ha, na.rm = TRUE)) %>%
  pull(desvpad)

soja_prod_desvpad <- df_soja %>% mutate(
  Produtividade_Sacas_ha = as.numeric(Produtividade_Sacas_ha)) %>%
  summarise(desvpad = sd(Produtividade_Sacas_ha, na.rm = TRUE)) %>%
  pull(desvpad)

# Insere a coluna prod_desvpad ao df_final
df_final <- df_final %>% mutate("prod_desvpad" = round(c(cafe_prod_desvpad, soja_prod_desvpad), 1))

# Cálculo da média + 1 desvpad e média - 1 desvpad
df_final <- df_final %>% mutate("prod_media_mais1_devpad" = prod_media + prod_desvpad)
df_final <- df_final %>% mutate("prod_media_menos1_devpad" = prod_media - prod_desvpad)

# Cálculo da produção total de café e soja
cafe_total_sacas <- df_cafe %>% mutate(
  Producao_Total_Sacas = as.numeric(Producao_Total_Sacas)) %>%
  summarise(producao_total = sum(Producao_Total_Sacas, na.rm = TRUE)) %>%
  pull(producao_total)

soja_total_sacas <- df_soja %>% mutate(
  Producao_Total_Sacas = as.numeric(Producao_Total_Sacas)) %>%
  summarise(producao_total = sum(Producao_Total_Sacas, na.rm = TRUE)) %>%
  pull(producao_total)

df_final <- df_final %>% mutate("producao_total" = round(c(cafe_total_sacas, soja_total_sacas)))

# Cálculo do consumo de Fósforo por ha e adiciona a média a df_final
df <- df %>% mutate("fosforo_ha" = Insumo_Fosforo_kg / Area_Total_ha)

cafe_fosforo_ha_med <- df[df$Cultura == "café", ] %>% summarise(fosforo_ha_med = round(mean(fosforo_ha), 1)) %>%
  pull(fosforo_ha_med)

soja_fosforo_ha_med <- df[df$Cultura == "soja", ] %>% summarise(fosforo_ha_med = round(mean(fosforo_ha), 1)) %>%
  pull(fosforo_ha_med)

df_final <- df_final %>% mutate("fosforo_ha_med" = c(cafe_fosforo_ha_med, soja_fosforo_ha_med))

# Cálculo de correlação tamanho da área e produtividade
# Café
cafe_area_prod_cor <- cor(df_cafe$Area_Total_ha, df_cafe$Produtividade_Sacas_ha, method = "pearson")
print(cafe_area_prod_cor)

# Soja
soja_area_prod_cor <- cor(df_soja$Area_Total_ha, df_soja$Produtividade_Sacas_ha, method = "pearson")
print(soja_area_prod_cor)

# Ordenação do df original por Producao_Total_Sacas
df <- df %>% arrange(desc(Producao_Total_Sacas))
print(df)
