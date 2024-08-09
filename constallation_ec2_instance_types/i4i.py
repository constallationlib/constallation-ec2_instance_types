from instance_type import InstanceType

i4i_large = InstanceType(
    instance_family="i4i",
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
    memory_gb=16.0,
    storage_gb=468,
    storage_type="NVMe SSD",
    network_performance="Up to 12.5 Gigabit",
    instance_storage_gb=468,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=3,
    ipv6_support=True
)

i4i_xlarge = InstanceType(
    instance_family="i4i",
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
    memory_gb=32.0,
    storage_gb=937,
    storage_type="NVMe SSD",
    network_performance="Up to 12.5 Gigabit",
    instance_storage_gb=937,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=3,
    ipv6_support=True
)

i4i_2xlarge = InstanceType(
    instance_family="i4i",
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
    memory_gb=64.0,
    storage_gb=1875,
    storage_type="NVMe SSD",
    network_performance="Up to 25 Gigabit",
    instance_storage_gb=1875,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=4,
    ipv6_support=True
)

i4i_4xlarge = InstanceType(
    instance_family="i4i",
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
    memory_gb=128.0,
    storage_gb=3750,
    storage_type="NVMe SSD",
    network_performance="Up to 25 Gigabit",
    instance_storage_gb=3750,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=8,
    ipv6_support=True
)

i4i_8xlarge = InstanceType(
    instance_family="i4i",
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
    memory_gb=256.0,
    storage_gb=7500,
    storage_type="NVMe SSD",
    network_performance="Up to 37.5 Gigabit",
    instance_storage_gb=7500,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=8,
    ipv6_support=True
)

i4i_16xlarge = InstanceType(
    instance_family="i4i",
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
    memory_gb=512.0,
    storage_gb=15000,
    storage_type="NVMe SSD",
    network_performance="Up to 75 Gigabit",
    instance_storage_gb=15000,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=15,
    ipv6_support=True
)

i4i_32xlarge = InstanceType(
    instance_family="i4i",
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
    memory_gb=1024.0,
    storage_gb=30000,
    storage_type="NVMe SSD",
    network_performance="100 Gigabit",
    instance_storage_gb=30000,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=50,
    ipv6_support=True
)

i4i_metal = InstanceType(
    instance_family="i4i",
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
    memory_gb=1024.0,
    storage_gb=30000,
    storage_type="NVMe SSD",
    network_performance="100 Gigabit",
    instance_storage_gb=30000,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=50,
    ipv6_support=True
)