mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"santi.viquez@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = process.env.PORT\n\
" > ~/.streamlit/config.toml