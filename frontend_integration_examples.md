# 🔌 Como Conectar a API FastScanNutri ao Frontend

## 📋 Informações da API

- **URL Base**: `http://127.0.0.1:8001`
- **Documentação**: `http://127.0.0.1:8001/docs`
- **Endpoints principais**:
  - `POST /analyze` - Análise nutricional
  - `GET /health` - Status da API
  - `GET /user/{user_id}/analyses` - Histórico do usuário

---

## 🌐 **JavaScript/TypeScript (React, Vue, Angular)**

### 1. Função para Analisar Imagem

```javascript
// Configuração da API
const API_BASE_URL = 'http://127.0.0.1:8001';

// Função para analisar imagem de alimento
async function analyzeFood(imageFile, userId, foodName = null) {
  try {
    const formData = new FormData();
    formData.append('image', imageFile);
    formData.append('user_id', userId);
    
    if (foodName) {
      formData.append('nome', foodName);
    }

    const response = await fetch(`${API_BASE_URL}/analyze`, {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      throw new Error(`Erro na API: ${response.status}`);
    }

    const result = await response.json();
    return result;
  } catch (error) {
    console.error('Erro ao analisar alimento:', error);
    throw error;
  }
}

// Função para buscar histórico do usuário
async function getUserHistory(userId) {
  try {
    const response = await fetch(`${API_BASE_URL}/user/${userId}/analyses`);
    
    if (!response.ok) {
      throw new Error(`Erro na API: ${response.status}`);
    }

    const history = await response.json();
    return history;
  } catch (error) {
    console.error('Erro ao buscar histórico:', error);
    throw error;
  }
}

// Função para verificar status da API
async function checkAPIHealth() {
  try {
    const response = await fetch(`${API_BASE_URL}/health`);
    return response.ok;
  } catch (error) {
    console.error('API não está disponível:', error);
    return false;
  }
}
```

### 2. Exemplo de Uso no React

```jsx
import React, { useState } from 'react';

function FoodAnalyzer() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [userId] = useState('user123'); // ID do usuário logado

  const handleFileSelect = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleAnalyze = async () => {
    if (!selectedFile) {
      alert('Selecione uma imagem primeiro!');
      return;
    }

    setLoading(true);
    try {
      const analysis = await analyzeFood(selectedFile, userId);
      setResult(analysis);
    } catch (error) {
      alert('Erro ao analisar alimento: ' + error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="food-analyzer">
      <h2>Análise Nutricional</h2>
      
      <input 
        type="file" 
        accept="image/*" 
        onChange={handleFileSelect}
        disabled={loading}
      />
      
      <button 
        onClick={handleAnalyze} 
        disabled={!selectedFile || loading}
      >
        {loading ? 'Analisando...' : 'Analisar Alimento'}
      </button>

      {result && (
        <div className="result">
          <h3>Resultado da Análise</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default FoodAnalyzer;
```

---

## 📱 **React Native**

```javascript
// api.js
const API_BASE_URL = 'http://127.0.0.1:8001'; // Para iOS Simulator
// const API_BASE_URL = 'http://10.0.2.2:8001'; // Para Android Emulator
// const API_BASE_URL = 'http://SEU_IP_LOCAL:8001'; // Para dispositivo físico

export async function analyzeFood(imageUri, userId, foodName = null) {
  const formData = new FormData();
  
  formData.append('image', {
    uri: imageUri,
    type: 'image/jpeg',
    name: 'food.jpg',
  });
  
  formData.append('user_id', userId);
  
  if (foodName) {
    formData.append('nome', foodName);
  }

  try {
    const response = await fetch(`${API_BASE_URL}/analyze`, {
      method: 'POST',
      body: formData,
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });

    const result = await response.json();
    return result;
  } catch (error) {
    console.error('Erro na análise:', error);
    throw error;
  }
}

// Componente de exemplo
import React from 'react';
import { View, Button, Image, Text } from 'react-native';
import { launchImageLibrary } from 'react-native-image-picker';

export function FoodAnalyzer() {
  const [imageUri, setImageUri] = useState(null);
  const [result, setResult] = useState(null);

  const selectImage = () => {
    launchImageLibrary({ mediaType: 'photo' }, (response) => {
      if (response.assets?.[0]) {
        setImageUri(response.assets[0].uri);
      }
    });
  };

  const analyzeImage = async () => {
    if (imageUri) {
      try {
        const analysis = await analyzeFood(imageUri, 'user123');
        setResult(analysis);
      } catch (error) {
        alert('Erro ao analisar: ' + error.message);
      }
    }
  };

  return (
    <View>
      <Button title="Selecionar Imagem" onPress={selectImage} />
      {imageUri && <Image source={{ uri: imageUri }} style={{ width: 200, height: 200 }} />}
      <Button title="Analisar" onPress={analyzeImage} disabled={!imageUri} />
      {result && <Text>{JSON.stringify(result, null, 2)}</Text>}
    </View>
  );
}
```

---

## 🐍 **Python (se usar Flask/Django)**

```python
import requests
import json

class NutritionAPI:
    def __init__(self, base_url="http://127.0.0.1:8001"):
        self.base_url = base_url
    
    def analyze_food(self, image_path, user_id, food_name=None):
        """Analisa uma imagem de alimento"""
        url = f"{self.base_url}/analyze"
        
        files = {'image': open(image_path, 'rb')}
        data = {'user_id': user_id}
        
        if food_name:
            data['nome'] = food_name
        
        try:
            response = requests.post(url, files=files, data=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return None
        finally:
            files['image'].close()
    
    def get_user_history(self, user_id):
        """Busca histórico de análises do usuário"""
        url = f"{self.base_url}/user/{user_id}/analyses"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return None

# Exemplo de uso
api = NutritionAPI()
result = api.analyze_food('caminho/para/imagem.jpg', 'user123', 'Maçã')
print(json.dumps(result, indent=2))
```

---

## 🔧 **Configurações Importantes**

### 1. CORS (Cross-Origin Resource Sharing)
Se estiver tendo problemas de CORS, verifique se a API tem as configurações corretas no `main.py`:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique os domínios
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 2. URLs para Diferentes Ambientes

- **Desenvolvimento Local**: `http://127.0.0.1:8001`
- **Rede Local**: `http://SEU_IP_LOCAL:8001`
- **Produção**: `https://seu-dominio.com`

### 3. Tratamento de Erros

Sempre implemente tratamento de erros adequado:

```javascript
try {
  const result = await analyzeFood(file, userId);
  // Sucesso
} catch (error) {
  if (error.message.includes('413')) {
    alert('Imagem muito grande. Tente uma imagem menor.');
  } else if (error.message.includes('422')) {
    alert('Formato de imagem não suportado.');
  } else {
    alert('Erro inesperado. Tente novamente.');
  }
}
```

---

## 🚀 **Próximos Passos**

1. **Escolha a tecnologia** do seu frontend
2. **Copie o código exemplo** correspondente
3. **Ajuste as URLs** conforme seu ambiente
4. **Teste a integração** com uma imagem
5. **Implemente o tratamento de erros**
6. **Adicione feedback visual** (loading, progress, etc.)

Se precisar de ajuda específica para sua tecnologia, me informe qual framework/linguagem você está usando!
