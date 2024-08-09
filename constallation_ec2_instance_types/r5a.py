from instance_type import InstanceType

r5a_large = InstanceType(
    instance_family="r5a",
    instance_size="large",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=2,
    architecture="x86_64",
    cores=2,
    valid_cores=[1, 2],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=2.5,
    memory_gb=16.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 10 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=3,
    ipv6_support=True
)

r5a_xlarge = InstanceType(
    instance_family="r5a",
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
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 10 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=3,
    ipv6_support=True
)

r5a_2xlarge = InstanceType(
    instance_family="r5a",
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
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 10 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=4,
    ipv6_support=True
)

r5a_4xlarge = InstanceType(
    instance_family="r5a",
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
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 10 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=4,
    ipv6_support=True
)

r5a_8xlarge = InstanceType(
    instance_family="r5a",
    instance_size="8xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=32,
    architecture="x86_64",
    cores=32,
    valid_cores=[8, 16, 32],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=2.5,
    memory_gb=256.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 10 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=8,
    ipv6_support=True
)

r5a_12xlarge = InstanceType(
    instance_family="r5a",
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
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 12.5 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=12,
    ipv6_support=True
)

r5a_16xlarge = InstanceType(
    instance_family="r5a",
    instance_size="16xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=64,
    architecture="x86_64",
    cores=64,
    valid_cores=[16, 32, 64],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=2.5,
    memory_gb=512.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 20 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=15,
    ipv6_support=True
)

r5a_24xlarge = InstanceType(
    instance_family="r5a",
    instance_size="24xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=96,
    architecture="x86_64",
    cores=96,
    valid_cores=[24, 48, 96],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=2.5,
    memory_gb=768.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 25 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=15,
    ipv6_support=True
)