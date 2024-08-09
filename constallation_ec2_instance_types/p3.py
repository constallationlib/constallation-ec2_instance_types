from instance_type import InstanceType

p3_2xlarge = InstanceType(
    instance_family="p3",
    instance_size="2xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=8,
    architecture="x86_64",
    cores=4,
    valid_cores=[2, 4, 8],
    threads_per_core=2,
    valid_threads_per_core=[1, 2],
    sustained_clock_speed=2.7,
    memory_gb=61.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 10 Gigabit",
    instance_storage_gb=None,
    gpu=True,
    gpu_count=1,
    gpu_memory_gb=16.0,
    eni=4,
    ipv6_support=True
)

p3_8xlarge = InstanceType(
    instance_family="p3",
    instance_size="8xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=32,
    architecture="x86_64",
    cores=16,
    valid_cores=[8, 16, 32],
    threads_per_core=2,
    valid_threads_per_core=[1, 2],
    sustained_clock_speed=2.7,
    memory_gb=244.0,
    storage_gb=None,
    storage_type=None,
    network_performance="10 Gigabit",
    instance_storage_gb=None,
    gpu=True,
    gpu_count=4,
    gpu_memory_gb=64.0,
    eni=8,
    ipv6_support=True
)

p3_16xlarge = InstanceType(
    instance_family="p3",
    instance_size="16xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=64,
    architecture="x86_64",
    cores=32,
    valid_cores=[16, 32, 64],
    threads_per_core=2,
    valid_threads_per_core=[1, 2],
    sustained_clock_speed=2.7,
    memory_gb=488.0,
    storage_gb=None,
    storage_type=None,
    network_performance="25 Gigabit",
    instance_storage_gb=None,
    gpu=True,
    gpu_count=8,
    gpu_memory_gb=128.0,
    eni=15,
    ipv6_support=True
)

p3dn_24xlarge = InstanceType(
    instance_family="p3dn",
    instance_size="24xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=96,
    architecture="x86_64",
    cores=48,
    valid_cores=[24, 48, 96],
    threads_per_core=2,
    valid_threads_per_core=[1, 2],
    sustained_clock_speed=2.7,
    memory_gb=768.0,
    storage_gb=1800,
    storage_type="NVMe SSD",
    network_performance="100 Gigabit",
    instance_storage_gb=1800.0,
    gpu=True,
    gpu_count=8,
    gpu_memory_gb=256.0,
    eni=15,
    ipv6_support=True
)