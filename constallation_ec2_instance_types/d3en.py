from instance_type import InstanceType

d3en_xlarge = InstanceType(
    instance_family="d3en",
    instance_size="xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=4,
    architecture="x86_64",
    cores=4,
    valid_cores=[2, 4],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=2.5,
    memory_gb=32.0,
    storage_gb=8000,
    storage_type="HDD",
    network_performance="Up to 25 Gigabit",
    instance_storage_gb=8000,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=3,
    ipv6_support=True
)

d3en_2xlarge = InstanceType(
    instance_family="d3en",
    instance_size="2xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=8,
    architecture="x86_64",
    cores=8,
    valid_cores=[2, 4, 8],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=2.5,
    memory_gb=64.0,
    storage_gb=16000,
    storage_type="HDD",
    network_performance="Up to 25 Gigabit",
    instance_storage_gb=16000,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=3,
    ipv6_support=True
)

d3en_4xlarge = InstanceType(
    instance_family="d3en",
    instance_size="4xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=16,
    architecture="x86_64",
    cores=16,
    valid_cores=[4, 8, 16],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=2.5,
    memory_gb=128.0,
    storage_gb=32000,
    storage_type="HDD",
    network_performance="Up to 25 Gigabit",
    instance_storage_gb=32000,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=3,
    ipv6_support=True
)

d3en_6xlarge = InstanceType(
    instance_family="d3en",
    instance_size="6xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=24,
    architecture="x86_64",
    cores=24,
    valid_cores=[6, 12, 24],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=2.5,
    memory_gb=192.0,
    storage_gb=48000,
    storage_type="HDD",
    network_performance="Up to 25 Gigabit",
    instance_storage_gb=48000,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=3,
    ipv6_support=True
)

d3en_12xlarge = InstanceType(
    instance_family="d3en",
    instance_size="12xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=48,
    architecture="x86_64",
    cores=48,
    valid_cores=[12, 24, 48],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=2.5,
    memory_gb=384.0,
    storage_gb=96000,
    storage_type="HDD",
    network_performance="50 Gigabit",
    instance_storage_gb=96000,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=3,
    ipv6_support=True
)