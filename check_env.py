# spark is pre-configured when this runs on a Databricks cluster — no setup needed.
 
df = spark.sql("select * from SNOWFLAKE_DB_TL_MFG_S.TL_MFG.ENT_IIOT_ATLASCO_PCO")
 
print(f"Row count: {df.count()}")
df.show(5)

# Runs on the gpu_cluster job cluster (15.4.x-gpu-ml-scala2.12, Standard_NC4as_T4_v3) — PyTorch ships preinstalled.
import torch
 
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
 
if torch.cuda.is_available():
    print(f"GPU device: {torch.cuda.get_device_name(0)}")
    x = torch.rand(4096, 4096, device="cuda")
    y = torch.rand(4096, 4096, device="cuda")
    z = x @ y
    torch.cuda.synchronize()
    print(f"Matrix multiply result shape: {tuple(z.shape)}, sum: {z.sum().item():.2f}")
else:
    print("No GPU detected — running on CPU only.")
    