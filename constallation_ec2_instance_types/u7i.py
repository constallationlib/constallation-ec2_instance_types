from instance_type import InstanceType

u7i_1tb = InstanceType(
    instance_family="u7i",
    instance_size="1tb",
    free_tier_eligible=False,
    bare_metal=True,
    hypervisor=None,  # No hypervisor for bare metal instances
    vcpus=128,
    architecture="x86_64",
    cores=64,
    valid_cores=[16, 32, 64, 128],
    threads_per_core=2,
    valid_threads_per_core=[1, 2],
    sustained_clock_speed=3.8,
    memory_gb=1024.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 100 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=60,
    ipv6_support=True
)

u7i_2tb = InstanceType(
    instance_family="u7i",
    instance_size="2tb",
    free_tier_eligible=False,
    bare_metal=True,
    hypervisor=None,  # No hypervisor for bare metal instances
    vcpus=128,
    architecture="x86_64",
    cores=64,
    valid_cores=[16, 32, 64, 128],
    threads_per_core=2,
    valid_threads_per_core=[1, 2],
    sustained_clock_speed=3.8,
    memory_gb=2048.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 100 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=60,
    ipv6_support=True
)

u7i_4tb = InstanceType(
    instance_family="u7i",
    instance_size="4tb",
    free_tier_eligible=False,
    bare_metal=True,
    hypervisor=None,  # No hypervisor for bare metal instances
    vcpus=128,
    architecture="x86_64",
    cores=64,
    valid_cores=[16, 32, 64, 128],
    threads_per_core=2,
    valid_threads_per_core=[1, 2],
    sustained_clock_speed=3.8,
    memory_gb=4096.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 100 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=60,
    ipv6_support=True
)

u7i_6tb = InstanceType(
    instance_family="u7i",
    instance_size="6tb",
    free_tier_eligible=False,
    bare_metal=True,
    hypervisor=None,  # No hypervisor for bare metal instances
    vcpus=128,
    architecture="x86_64",
    cores=64,
    valid_cores=[16, 32, 64, 128],
    threads_per_core=2,
    valid_threads_per_core=[1, 2],
    sustained_clock_speed=3.8,
    memory_gb=6144.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 100 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=60,
    ipv6_support=True
)

u7i_12tb = InstanceType(
    instance_family="u7i",
    instance_size="12tb",
    free_tier_eligible=False,
    bare_metal=True,
    hypervisor=None,  # No hypervisor for bare metal instances
    vcpus=128,
    architecture="x86_64",
    cores=64,
    valid_cores=[16, 32, 64, 128],
    threads_per_core=2,
    valid_threads_per_core=[1, 2],
    sustained_clock_speed=3.8,
    memory_gb=12288.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 100 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=60,
    ipv6_support=True
)