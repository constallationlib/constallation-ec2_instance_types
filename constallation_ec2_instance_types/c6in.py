from instance_type import InstanceType

c6in_large = InstanceType(
    instance_family="c6in",
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
    sustained_clock_speed=3.5,
    memory_gb=4.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 25 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=3,
    ipv6_support=True
)

c6in_xlarge = InstanceType(
    instance_family="c6in",
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
    sustained_clock_speed=3.5,
    memory_gb=8.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 25 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=3,
    ipv6_support=True
)

c6in_2xlarge = InstanceType(
    instance_family="c6in",
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
    sustained_clock_speed=3.5,
    memory_gb=16.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 25 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=4,
    ipv6_support=True
)

c6in_4xlarge = InstanceType(
    instance_family="c6in",
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
    sustained_clock_speed=3.5,
    memory_gb=32.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 30 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=4,
    ipv6_support=True
)

c6in_8xlarge = InstanceType(
    instance_family="c6in",
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
    sustained_clock_speed=3.5,
    memory_gb=64.0,
    storage_gb=None,
    storage_type=None,
    network_performance="50 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=8,
    ipv6_support=True
)

c6in_12xlarge = InstanceType(
    instance_family="c6in",
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
    sustained_clock_speed=3.5,
    memory_gb=96.0,
    storage_gb=None,
    storage_type=None,
    network_performance="75 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=12,
    ipv6_support=True
)

c6in_16xlarge = InstanceType(
    instance_family="c6in",
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
    sustained_clock_speed=3.5,
    memory_gb=128.0,
    storage_gb=None,
    storage_type=None,
    network_performance="100 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=15,
    ipv6_support=True
)

c6in_32xlarge = InstanceType(
    instance_family="c6in",
    instance_size="32xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=128,
    architecture="x86_64",
    cores=128,
    valid_cores=[32, 64, 128],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=3.5,
    memory_gb=256.0,
    storage_gb=None,
    storage_type=None,
    network_performance="200 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=50,
    ipv6_support=True
)

c6in_metal = InstanceType(
    instance_family="c6in",
    instance_size="metal",
    free_tier_eligible=False,
    bare_metal=True,
    hypervisor=None,  # No hypervisor for bare metal instances
    vcpus=128,
    architecture="x86_64",
    cores=128,
    valid_cores=[32, 64, 128],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=3.5,
    memory_gb=256.0,
    storage_gb=None,
    storage_type=None,
    network_performance="200 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=50,
    ipv6_support=True
)