import time
import requests
import json

# Configuration
OLLAMA_URL = "http://ollama.demo-w04-s009:11434/v1/chat/completions"
MODEL = "qwen3:0.6b"
TEST_PROMPT = "Write a detailed explanation about quantum computing and its applications."

def benchmark_ollama(num_runs=5):
    """
    Benchmarks the Ollama instance by making multiple requests
    and calculating average tokens per second.
    """
    results = []
    
    for i in range(num_runs):
        print(f"\nRun {i+1}/{num_runs}...")
        
        # Prepare the request
        payload = {
            "model": MODEL,
            "messages": [
                {"role": "user", "content": TEST_PROMPT}
            ],
            "stream": False,
            "temperature": 0.7,
            "max_tokens": 500  # Adjust as needed
        }
        
        # Time the request
        start_time = time.time()
        response = requests.post(OLLAMA_URL, json=payload)
        end_time = time.time()
        
        # Parse response
        if response.status_code == 200:
            data = response.json()
            
            # Extract token counts and timing
            tokens_generated = data['usage']['completion_tokens']
            total_time = end_time - start_time
            tokens_per_second = tokens_generated / total_time
            
            results.append({
                'tokens': tokens_generated,
                'time': total_time,
                'tokens_per_second': tokens_per_second
            })
            
            print(f"  Tokens: {tokens_generated}")
            print(f"  Time: {total_time:.2f}s")
            print(f"  Speed: {tokens_per_second:.2f} tokens/s")
        else:
            print(f"  Error: {response.status_code}")
    
    # Calculate averages
    if results:
        avg_tokens = sum(r['tokens'] for r in results) / len(results)
        avg_time = sum(r['time'] for r in results) / len(results)
        avg_tps = sum(r['tokens_per_second'] for r in results) / len(results)
        
        print("\n" + "="*50)
        print("BENCHMARK RESULTS")
        print("="*50)
        print(f"Average tokens generated: {avg_tokens:.0f}")
        print(f"Average time: {avg_time:.2f}s")
        print(f"Average speed: {avg_tps:.2f} tokens/second")
        print("="*50)

if __name__ == "__main__":
    benchmark_ollama(num_runs=5)