from instance_type import InstanceType

mac_metal = InstanceType(
    instance_family="mac",
    instance_size="metal",
    free_tier_eligible=False,
    bare_metal=True,
    hypervisor=None,  # No hypervisor for bare metal instances
    vcpus=12,
    architecture="x86_64",
    cores=12,
    valid_cores=[12],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=3.2,
    memory_gb=32.0,
    storage_gb=300.0,
    storage_type="NVMe SSD",
    network_performance="Up to 10 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=1,
    ipv6_support=True
)
