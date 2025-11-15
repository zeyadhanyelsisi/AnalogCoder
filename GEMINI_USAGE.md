# Using Gemini with AnalogCoder

## Setup

1. **Get your Gemini API key** from [Google AI Studio](https://aistudio.google.com/apikey)

2. **Install the required package** (already done):
   ```bash
   pip install google-generativeai
   ```

## Usage

### Command-line Example:

```bash
# Activate environment
source analog_env/bin/activate

# Run with Gemini 1.5 Flash (Recommended - Fast & Free)
python gpt_run.py \
  --model="gemini-1.5-flash" \
  --task_id=1 \
  --api_key="YOUR_GEMINI_API_KEY_HERE" \
  --num_per_task=1

# Or with Gemini 1.5 Pro (More capable, slower)
python gpt_run.py \
  --model="gemini-1.5-pro" \
  --task_id=1 \
  --api_key="YOUR_GEMINI_API_KEY_HERE" \
  --num_per_task=1
```

### Supported Gemini Models:
- `gemini-1.5-flash` - **Recommended** - Fast, efficient, free tier
- `gemini-1.5-pro` - Most capable, larger context window
- `gemini-2.0-flash-exp` - Experimental newest version
- ~~`gemini-pro`~~ - Deprecated (automatically mapped to gemini-1.5-flash)

### Notes:
- Gemini API is **free** with generous quotas for personal use
- The code automatically handles the different message format between OpenAI and Gemini
- Cost tracking is not implemented for Gemini (set to 0)
- Temperature and other generation parameters work the same way

### Complete Example:

```bash
cd /mnt/c/Users/z004hj6s/Thesis_Work/AnalogCoder_forked/AnalogCoder
source analog_env/bin/activate
python gpt_run.py --model="gemini-1.5-flash" --task_id=1 --api_key="YOUR_KEY" --num_per_task=1
```

This will generate a single-stage common-source amplifier using Gemini!
