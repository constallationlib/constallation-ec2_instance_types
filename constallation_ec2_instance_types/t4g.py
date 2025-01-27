from instance_type import InstanceType

t4g_nano = InstanceType(
    instance_family="t4g",
    instance_size="nano",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=2,
    architecture="arm64",
    cores=1,
    valid_cores=[1],
    threads_per_core=2,
    valid_threads_per_core=[1, 2],
    sustained_clock_speed=2.5,  # burstable
    memory_gb=0.5,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 5 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=2,
    ipv6_support=True
)

t4g_micro = InstanceType(
    instance_family="t4g",
    instance_size="micro",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=2,
    architecture="arm64",
    cores=1,
    valid_cores=[1],
    threads_per_core=2,
    valid_threads_per_core=[1, 2],
    sustained_clock_speed=2.5,  # burstable
    memory_gb=1.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 5 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=2,
    ipv6_support=True
)

t4g_small = InstanceType(
    instance_family="t4g",
    instance_size="small",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=2,
    architecture="arm64",
    cores=1,
    valid_cores=[1],
    threads_per_core=2,
    valid_threads_per_core=[1, 2],
    sustained_clock_speed=2.5,  # burstable
    memory_gb=2.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 5 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=3,
    ipv6_support=True
)

t4g_medium = InstanceType(
    instance_family="t4g",
    instance_size="medium",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=2,
    architecture="arm64",
    cores=1,
    valid_cores=[1],
    threads_per_core=2,
    valid_threads_per_core=[1, 2],
    sustained_clock_speed=2.5,  # burstable
    memory_gb=4.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 5 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=3,
    ipv6_support=True
)

t4g_large = InstanceType(
    instance_family="t4g",
    instance_size="large",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=2,
    architecture="arm64",
    cores=1,
    valid_cores=[1],
    threads_per_core=2,
    valid_threads_per_core=[1, 2],
    sustained_clock_speed=2.5,  # burstable
    memory_gb=8.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 5 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=3,
    ipv6_support=True
)

t4g_xlarge = InstanceType(
    instance_family="t4g",
    instance_size="xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=4,
    architecture="arm64",
    cores=2,
    valid_cores=[1, 2],
    threads_per_core=2,
    valid_threads_per_core=[1, 2],
    sustained_clock_speed=2.5,  # burstable
    memory_gb=16.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 5 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=3,
    ipv6_support=True
)

t4g_2xlarge = InstanceType(
    instance_family="t4g",
    instance_size="2xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=8,
    architecture="arm64",
    cores=4,
    valid_cores=[1, 2, 4],
    threads_per_core=2,
    valid_threads_per_core=[1, 2],
    sustained_clock_speed=2.5,  # burstable
    memory_gb=32.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 5 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=4,
    ipv6_support=True
)
